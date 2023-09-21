# Stores all routes
import json
from sqlalchemy.sql import func
from application import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from application.form import userinput
from application.models import incomexpense


@app.route('/')
def home():
    income_vs_expense = db.session.query(func.sum(incomexpense.amount), incomexpense).group_by(incomexpense.type).order_by(incomexpense.type).all()  
    category_comparison = db.session.query(db.func.sum(incomexpense.amount), incomexpense.category).group_by(incomexpense.category).order_by(incomexpense.category).all()
    dates = db.session.query(func.sum(incomexpense.amount), incomexpense.date).group_by(incomexpense.date).order_by(incomexpense.date).all()
    entries = incomexpense.query.order_by(incomexpense.date.desc()).all()

    income_expense = []
    for total_amount, _ in income_vs_expense:
        income_expense.append(total_amount)

    income_category = []
    for amounts, _ in category_comparison:
        income_category.append(amounts)

    over_time_expenditure = []
    date_labels = []
    for amount, date in dates:
        over_time_expenditure.append(amount)
        date_labels.append(date.strftime("%d-%m-%Y"))

    return(render_template('dashboard.html',
                           title = 'Dashboard',
                           entries = entries,
                           income_vs_expense = json.dumps(income_expense),
                           over_time_expenditure = json.dumps(over_time_expenditure),
                           income_category=json.dumps(income_category),
                           date_labels = json.dumps(date_labels)))

@app.route('/layout')
def layout():
    return(render_template('layout.html'))

@app.route('/delete/<int:entry_id>')
def delete(entry_id):
    entry = incomexpense.query.get_or_404((int(entry_id)))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted successfully")
    return(redirect(url_for('home')))

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = userinput()
    if form.validate_on_submit():
        entry = incomexpense(type = form.type.data, amount = form.amount.data, category = form.category.data)
        db.session.add(entry)
        db.session.commit()
        flash("Entry added successfully")
        return(redirect(url_for('home')))

    return(render_template('add.html', title = 'Add', form = form))