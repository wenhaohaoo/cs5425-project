db = new Mongo().getDB("tweets");
db.createCollection("sg");
db.createCollection("hk");
db.createCollection("au");
db.sg.createIndex({created_at: 1})
db.hk.createIndex({created_at: 1})
db.au.createIndex({created_at: 1})