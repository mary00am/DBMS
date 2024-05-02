from flask import Flask, request
import dbconn
import uuid
app = Flask(__name__)
print(uuid.uuid4())
db = dbconn.DBConn()

@app.route('/books',methods=['GET'])
def getbooks():
    if db.connect_to_postgresql():
        result = db.executeQuery('SELECT * FROM lib.books;')
        return {'result':result}
    else:
        print('error connecting to database')
        return {'result':'500 database error'}
@app.route('/books',methods=['POST'])
def postbooks():
    if db.connect_to_postgresql():
        values = request.args
        print(values,11)
        if values['bookId'] and values['genreId'] and values['title'] and values['authorId'] and values['publisher'] and values['ISBNNumber']:
            result = db.executeQuery('INSERT INTO lib.books VALUES (%s, %s, %s,%s,%s,%s);',
                                 (values['bookId'],values['genreId'],values['title'],values['authorId'],
                                  values['publisher'],values['ISBNNumber']))
            return {'result': result}
        else:
            return {'result':'invalid fields'}
    else:
        print('error connecting to database')
        return {'result':'500 database error'}
@app.route('/books/<id>',methods=['GET'])
def getbooksById(id):
    if db.connect_to_postgresql():
        result = db.executeQuery("SELECT * FROM lib.books WHERE bookid=%s;",(id))
        return {'result':result}
    else:
        print('error connecting to database')
        return {'result':'500 database error'}
@app.route('/books/<id>',methods=['DELETE'])
def delbooks(id):
    if db.connect_to_postgresql():
        result = db.executeQuery("DELETE FROM lib.books WHERE bookid=%s;",(id))
        return {'result':result}
    else:
        print('error connecting to database')
        return {'result':'500 database error'}

@app.route('/borrowings',methods=['GET'])
def getborrowings():
    if db.connect_to_postgresql():
        result = db.executeQuery('SELECT * FROM lib.borrowings;')
        return {'result':result}
    else:
        print('error connecting to database')
        return {'result':'500'}
@app.route('/borrowings/<id>',methods=['GET'])
def getborrowingsById(id):
    if db.connect_to_postgresql():
        result = db.executeQuery("SELECT * FROM lib.borrowings WHERE borrowingid=%s;",(id))
        return {'result':result}
    else:
        print('error connecting to database')
        return {'result':'500'}
@app.route('/borrowings',methods=['POST'])
def postborrowings():
    if db.connect_to_postgresql():
        values = request.args
        print(values,11)
        if values['borrowingId'] and values['bookId'] and values['memberId'] and values['borrowDate'] and values['returnDate'] and values['dueDate']:
            result = db.executeQuery('INSERT INTO lib.borrowings VALUES (%s, %s, %s,%s,%s,%s);',
                                     (values['borrowingId'],values['bookId'],values['memberId'],values['borrowDate'],
                                      values['returnDate'],values['dueDate']))
            return {'result': result}
        else:
            return {'result':'invalid fields'}
    else:
        print('error connecting to database')
        return {'result':'500 database error'}
@app.route('/borrowings/<id>',methods=['DELETE'])
def delborrowings(id):
    if db.connect_to_postgresql():
        result = db.executeQuery("DELETE FROM lib.borrowings WHERE borrowingId=%s;",(id))
        return {'result':result}
    else:
        print('error connecting to database')
        return {'result':'500 database error'}

@app.route('/genres',methods=['GET','POST'])
def getgenres():
    if db.connect_to_postgresql():
        if request.method == 'POST':
            pass
        else:
            result = db.executeQuery('SELECT * FROM lib.genres;')
            return {'result':result}
    else:
        print('error connecting to database')
        return {'result':'500'}

@app.route('/genres/<id>',methods=['GET'])
def getgenresById(id):
    if db.connect_to_postgresql():
        result = db.executeQuery('SELECT * FROM lib.genres WHERE genreid=%s;',(id))
        return {'result':result}
    else:
        print('error connecting to database')
        return {'result':'500'}
@app.route('/genres',methods=['POST'])
def postborrowings():
    if db.connect_to_postgresql():
        values = request.args
        print(values,11)
        if values['genreId'] and values['genreName'] and values['description']:
            result = db.executeQuery('INSERT INTO lib.genres VALUES (%s, %s, %s);',
                                     (values['genreId'],values['genreName'],values['description']))
            return {'result': result}
        else:
            return {'result': 'invalid fields'}

    else:
        print('error connecting to database')
        return {'result':'500 database error'}
@app.route('/genres/<id>',methods=['DELETE'])
def delgenres(id):
    if db.connect_to_postgresql():
        result = db.executeQuery("DELETE FROM lib.genres WHERE genreid=%s;",(id))
        return {'result':result}
    else:
        print('error connecting to database')
        return {'result':'500 database error'}

@app.route('/members',methods=['GET'])
def getmembers():
    if db.connect_to_postgresql():
        result = db.executeQuery('SELECT * FROM lib.members;')
        return {'result':result}
    else:
        print('error connecting to database')
        return {'result':'500'}
@app.route('/members/<id>',methods=['GET'])
def getmembersById(id):
    if db.connect_to_postgresql():
        result = db.executeQuery('SELECT * FROM lib.members WHERE memberid=%s;',(id))
        return {'result':result}
    else:
        print('error connecting to database')
        return {'result':'500'}
@app.route('/members',methods=['POST'])
def postmembers():
    if db.connect_to_postgresql():
        values = request.args
        if values['memberId'] and values['name'] and values['contactNumber']:
            result = db.executeQuery('INSERT INTO lib.members VALUES (%s, %s, %s);',
                                     (values['memberId'],values['name'],values['contactNumber']))
            return {'result':result}
        else:
            return {'result':'invalid fields'}
    else:
        print('error connecting to database')
        return {'result':'500'}
@app.route('/members/<id>',methods=['DELETE'])
def delmembers(id):
    if db.connect_to_postgresql():
        result = db.executeQuery("DELETE FROM lib.members WHERE memberid=%s;",(id))
        return {'result':result}
    else:
        print('error connecting to database')
        return {'result':'500 database error'}

@app.route('/publishers',methods=['GET','POST'])
def getpublishers():
    if db.connect_to_postgresql():
        if request.method == 'POST':
            pass
        else:
            result = db.executeQuery('SELECT * FROM lib.publishers;')
            return {'result':result}
    else:
        print('error connecting to database')
        return {'result':'500'}

@app.route('/publishers/<id>',methods=['GET'])
def getpublishersById(id):
    if db.connect_to_postgresql():
        result = db.executeQuery('SELECT * FROM lib.publishers WHERE publisherId=%s;',(id))
        return {'result':result}
    else:
        print('error connecting to database')
        return {'result':'500'}
@app.route('/publishers',methods=['POST'])
def postborrowings():
    if db.connect_to_postgresql():
        values = request.args
        print(values,11)
        if values['publisherId'] and values['publisherName'] and values['location']:
            result = db.executeQuery('INSERT INTO lib.publishers VALUES (%s, %s, %s);',
                                     (values['publisherId'],values['publisherName'],values['location']))
            return {'result': result}
        else:
            return {'result':'invalid fields'}
    else:
        print('error connecting to database')
        return {'result':'500 database error'}
@app.route('/publishers/<id>',methods=['DELETE'])
def delpublishers(id):
    if db.connect_to_postgresql():
        result = db.executeQuery("DELETE FROM lib.publishers WHERE publisherId=%s;",(id))
        return {'result':result}
    else:
        print('error connecting to database')
        return {'result':'500 database error'}
app.run(host='127.0.0.1',port=3000)