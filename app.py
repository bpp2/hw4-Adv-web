from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from company")
    data=cur.fetchall()
    return render_template("index.html",datas=data)

@app.route("/add_company",methods=['POST','GET'])
def add_company():
    if request.method=='POST':
        cname=request.form['cname']
        email=request.form['email']
        contact=request.form['contact']
        address=request.form['address']
        con=sql.connect("db_web.db")
        cur=con.cursor()
        cur.execute("insert into company(CNAME,EMAIL,CONTACT, ADDRESS) values (?,?,?,?)",(cname,email,contact,address))
        con.commit()
        flash('Company Details Added','success')
        return redirect(url_for("home"))
    return render_template("add_company.html")

@app.route("/edit_company/<string:uid>",methods=['POST','GET'])
def edit_company(uid):
    if request.method=='POST':
        cname=request.form['cname']
        email=request.form['email']
        contact=request.form['contact']
        address=request.form['address']
        con=sql.connect("db_web.db")
        cur=con.cursor()
        cur.execute("update company set CNAME=?,CONTACT=?,Email=?,ADDRESS=? where UID=?",(cname,contact,email,address,uid))
        con.commit()
        flash('Company Details Updated','success')
        return redirect(url_for("home"))
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from company where UID=?",(uid,))
    data=cur.fetchone()
    return render_template("edit_company.html", datas=data)
    
@app.route("/delete_company/<string:uid>",methods=['GET'])
def delete_company(uid):
    con=sql.connect("db_web.db")
    cur=con.cursor()
    cur.execute("delete from company where UID=?",(uid,))
    con.commit()
    flash('Company Details Deleted','warning')
    return redirect(url_for("home"))
    
if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True)


