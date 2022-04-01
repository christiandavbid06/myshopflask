from flask import redirect, render_template, url_for, flash, request
from shop import db, app
from .models import Brand, Category

@app.route('/addbrand', methods=['GET','POST'])
def addbrand():
    if request.method=='POST':
        getBrand = request.form.get('brand')
        brand = Brand(name=getBrand)
        db.session.add(brand)
        flash(f'The brand {getBrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', brands='brands')

@app.route('/addcategory', methods=['GET','POST'])
def addcategory():
    if request.method=='POST':
        getCategory = request.form.get('category')
        category = Category(name=getCategory)
        db.session.add(category)
        flash(f'The category {getCategory} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addcategory'))
    return render_template('products/addbrand.html')