
# 指定資料集
#data = users

movie_list=[]
data = {}
#username2id = {}
userid2name = {}
movieid2name = {}



from math import sqrt
import operator
from operator import itemgetter


from engine.models import Rating
from engine.models import Movie
#from engine.models import User
from django.contrib.auth.models import User

# 推薦系統類別
class Recommender:
    
    def __init__(self, k=1, metric='cosine', n=2):
        '''
        類別欄位:   讓使用者可以設定的參數
        找到k個鄰居
        推薦n個樂團
        採用metric相似度公式
        資料集名稱data (先使用在外部的data)
        '''
        self.k = k
        self.n = n
        self.metric = metric
        
        if self.metric == 'pearson':
            self.fn = self.pearson
        elif self.metric == 'cosine':
            self.fn = self.cosine
        
        #self.data = data
        #self.loadMovie()
        self.loadMovieFromDB()
        self.load_movie_list()
        self.generate_like_dislike()
        print("成功new recommender！")

    # 新增使用者的評分到資料集
    def adduser(self, user_name, ratings):
        data[user_name]= ratings


    def recommend2(self,username):
        # 找到最接近的第一個人
        nearest = self.getNearestNeighbor(username)[0][0]
        recommendations = []
        # 找到nearest的評分的樂團當中 目標使用者沒有評分過的樂團
        neighborRatings = data[nearest]
        userRatings = data[username]
        for artist in neighborRatings:
            if not artist in userRatings:
                recommendations.append((artist, neighborRatings[artist]))
        # 排序      
        sorted_recm = sorted(recommendations, key=operator.itemgetter(1),  reverse=True)
        return sorted_recm[:self.n]  #self.n

    # 推薦  找多位鄰居  加權計算 樂團的分數
    def recommend(self, username): 
        recommendations = {}
        neighbors = self.getNearestNeighbor(username)
        #這位使用者的評分
        userRatings = data[username]

        # 計算　k位鄰居的　距離總和　計算權重之用
        k=3
        totalDistance = 0.0
        for i in range(k):
            totalDistance += neighbors[i][1]


        for i in range(k):
            # 計算距離權重 餅的面積 
            weight = neighbors[i][1] / totalDistance
            # 鄰居姓名
            name = neighbors[i][0]
            # 鄰居評分
            neighborRatings = data[name]

            # 推薦 樂團 給目標使用者--那些 鄰居評分過 但目標使用者尚未看過 的樂團
            for movie in neighborRatings:
                if not movie in userRatings:

                    if movie not in recommendations:
                        recommendations[movie] = neighborRatings[movie]* weight
                    else:
                        recommendations[movie] += neighborRatings[movie] * weight

        # 輸出為list [('飛兒', 4.4196),...]
        rcmd_list = [(movie, v ) for (movie, v) in recommendations.items()]

        # 排序 
        sorted_rcmd = sorted(rcmd_list, key=itemgetter(1),  reverse=True)

        # Return the first n items
        n=5
        return sorted_rcmd[: n]

    def getNearestNeighbor(self,username):
        distances = []
        for user in data:
            if user != username: 
                distance = self.fn(data[user], data[username])          
                distances.append(   (user, distance)  )
        # 依據距離排序 由大排到小cosine, pearson 越大越接近
        # 依據距離排序 由大排到小cosine, pearson 越大越接近
        sorted_distances = sorted(distances, key = itemgetter(1), reverse=True) 
        return sorted_distances[: self.k] # self.k = 3

    def cosine(self,rating1, rating2):
        sum_xy = 0
        sum_x2 = 0
        sum_y2 = 0
        for key in rating1:
            x = rating1[key]
            sum_x2 += pow(x, 2)
            if key in rating2:
                y = rating2[key]
                sum_xy += x * y

        for key in rating2:
            y = rating2[key]
            sum_y2 += pow(y, 2)    

            # now compute denominator
        denominator = sqrt(sum_x2) * sqrt(sum_y2)
        if denominator == 0:
            return 0
        else:
            return sum_xy / denominator

    def generate_like_dislike(self):
        #Step1:準備好喜歡 不喜歡 字典
        self.like={}
        self.dislike={}
        for i in movie_list:    
            movie_like = {}
            movie_dislike = {}
            for j in movie_list:
                movie_like[j] = 0
                movie_dislike[j]=0
            self.like[i] = movie_like
            self.dislike[i] = movie_dislike
        #Step2:統計次數
        for user in data: #每個人的評分
            for bi,vi in data[user].items(): #for評分的每個movie
                for bj, vj in data[user].items(): #for評分的每個movie
                    if bi != bj:
                        if vi >= 3 and vj >=3:
                            self.like[bi][bj] += 1
                        elif vi < 3 and vj < 3:
                            self.dislike[bi][bj]+=1
        #return like, dislike

        
    def also_like(self,movie):
        result = self.like[movie]
        sorted_result = sorted(result.items(), key=itemgetter(1), reverse=True)
        return sorted_result[: 5]
    def also_dislike(self,movie):
        result = self.dislike[movie]
        sorted_result = sorted(result.items(), key=itemgetter(1), reverse=True)
        return sorted_result[: 5]

    def loadMovie(self):
        path = './data_movie_ratings/'
        #(1)讀樂團檔案movie.csv  存放在 movieid2name字典
        #f = open(path + "movie.csv")
        f = open(path + "movie_台灣樂團.csv", encoding='UTF-8')
        for line in f:
            #separate line into fields
            fields = line.split(',')
            movie_id = fields[0].strip()
            movie_title = fields[1].strip()
            movieid2name[movie_id] = movie_title
        f.close()

        #(2)讀使用者檔案user.csv  存放在 userid2name, username2id字典      
        f = open(path + "user.csv")
        for line in f:
            fields = line.split(',')
            user_id = fields[0].strip()
            user_name = fields[1].strip()
            userid2name[user_id] = user_name
            #username2id[user_name] = user_id
        f.close()

        #
        #(3)讀使用者評分檔案rating.csv  存放在 data 字典
        # 不使用csv讀入,採用一行一行讀進來的方式,利於將欄位存放到字典內
        f = open(path + "rating.csv")
        for line in f:
            #separate line into fields--資料格式長這樣 1,11,3.5
            fields = line.split(',')

            # 取得編號
            user_id = fields[0].strip()
            movie_id = fields[1].strip()
            # 轉成編號對應的姓名
            user_name = userid2name[user_id]
            movie_name   = movieid2name[movie_id]
            # 取得評分
            rating = float(fields[2])
            # 加入data字典
            if user_name in data:
                currentRatings = data[user_name] #拿出已經放入的使用者評分
            else:
                currentRatings = {}
            currentRatings[movie_name] = rating #新增加入這個樂團的評分
            data[user_name] = currentRatings #新增後 更新(放回去)這個使用者評分
        f.close()      
        print("檔案讀取並轉成字典成功!")

    def load_movie_list(self):
        for b in Movie.objects.all():
            movie_list.append(b.name)


    def loadMovieFromDB(self):
        #data = {}    
        for rate in Rating.objects.all():
            # 對應的姓名 樂團名
            user_name = rate.user.username
            movie_name = rate.movie.name
            # 取得評分
            rating = rate.rating
            # 加入data字典
            if user_name in data:
                currentRatings = data[user_name] #拿出已經放入的使用者評分
            else:
                currentRatings = {}
            currentRatings[movie_name] = rating #新增加入這個樂團的評分
            data[user_name] = currentRatings #新增後 更新(放回去)這個使用者評分
        print("從資料庫讀取資料並轉成字典成功!")