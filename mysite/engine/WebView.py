'''
由於表格需#(1,2,3 ~)編號，測試其他方法皆不太適合。
1.查詢時加入編號 →→ 可以使用但編號會錯，由於會依造評價最高分排序，無法事前加入編號。
2.使用Jinja2語法設定變數 →→ Djago 使用Jinja2，但預設沒支援設定複雜。
3.抓取值context將dict資料加入編號。
'''
class WebView:

    def add_Index(self, data):
        dict1 = data
        list1 = list(dict1.values()) #access dict values && convert to list
        cnt_Index = 1 #set counter as id
        tuple_Box = []
        for list2 in list1:
            for tuple1 in list2:
                list3 = list(tuple1) #because the turple doesn't add number, convert to list
                list3.append(cnt_Index)
                tuple2 = tuple(list3)
                tuple_Box.append(tuple2)
                cnt_Index += 1
                # print (tuple2)
        return tuple_Box



    
