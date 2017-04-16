# coding=utf-8
""" '/books' Views """
from flask import Blueprint, render_template, abort, session
import tools

blueprint = Blueprint('books', __name__, url_prefix="/books")


@blueprint.route('/')
def display_all_books():
    """ Display All Books """
    pass


@blueprint.route('/<isbn>')
def display_book(isbn):
    """ Display a specific book based on the ISBN number
    :param isbn: isbn Number (10-digit / 13-digit)
    """

    # TODO: MongoDB Exceptions
    book = tools.get_book(isbn)

    if not book:
        abort(404)

    seller_list = tools.query_sales_listing(isbn)
    session['isbn_value'] = isbn
    return render_template('book/book_isbn.html', book=book, seller_list=seller_list)