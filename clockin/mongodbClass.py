import pymongo
import datetime


class MongoDB:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["app_v0"]
    # 获取用户账号

    def getAccount(self, type="lixinren"):
        account = self.db["account"]
        result = account.find({"type": type})
        json = {}
        for x in result:
            json = x
        return json
    # 更新用户账号cookie

    def updateAccount(self, params):
        account = self.db["account"]
        query = {"type": params["type"]}
        newvalues = {"$set": {"cookie": params["cookie"]}}
        x = account.update_one(query, newvalues)
        print(x.modified_count, "修改cookie成功")
    # 获取默认配置

    def getDefaultSetting(self):
        col = self.db["defaultSetting"]
        result = col.find_one()
        return result

    # 每天10点钟更新数据库数据--指数数据
    def updateIndexDataByDay(self, data):
        col = self.db['indexData']
        result = col.insert_many(data)
        print(datetime.datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S'), '插入数据结果---->完成：总共'+str(len(data))+'条，插入', len(result.inserted_ids))

    # 添加定投记录
    def getInvestRecord(self, parmas):
        col = self.db['investRecord']
        result = col.find()
        json = {}
        sort_type = parmas.get('sort', 'name')
        for i in result:
            i['_id'] = str(i['_id'])
            if i.get(sort_type) in json:

                json[i.get(sort_type)].append(i)
            else:
                json[i.get(sort_type)] = []
                json[i.get(sort_type)].append(i)
        arr = []
        if sort_type == 'code':
            for i in json:
                item = json[i][0]
                ijson = {
                    'name': item.get('name'),
                    'code': item.get('code'),
                    'num': 0,
                    'money': 0,
                }
                for j in json[i]:
                    ijson['money'] += float(j.get('money', 0))
                    ijson['num'] += float(j.get('num', 0))
                ijson['price'] = ijson['money']/ijson['num']
                arr.append(ijson)
        elif sort_type == 'date':
            for i in json:
                item = json[i][0]
                ijson = {
                    'date': i,
                    'code': json[i],
                    'money': 0,
                    'codeNum': len(json[i])
                }
                for j in json[i]:
                    ijson['money'] += float(j.get('money', 0))
                arr.append(ijson)
        return arr


# db = MongoDB()
# print(db.getInvestRecord({'sort': 'date'}))
