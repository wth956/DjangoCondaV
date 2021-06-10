

# dict1 = {'result': [(119, 'Star Wars', 4.6086956521739131), (116, 'Shawshank Redemption', 4.5), (120, 'The Dark Knight', 4.4210526315789478), (123, 'Toy Story', 4.2800000000000002), (106, 'Forest Gump', 4.208333333333333)]}
# list1 = list(dict1.values())
# print (list1)
class WebView:
    
    def __init__(self):


    def add_Index(self, dataset):
        cnt_Index = 1
        tuple_Box = []
        for list2 in list1:
            for tuple1 in list2:
                list3 = list(tuple1)
                list3.append(cnt_Index)
                tuple2 = tuple(list3)
                tuple_Box.append(tuple2)
                cnt_Index += 1
                # print (tuple2)
        print (tuple_Box)


    
