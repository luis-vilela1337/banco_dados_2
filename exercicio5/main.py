from database import Database
from writeAJson import writeAJson
from BookModel import BookModel
from cli import BookCLI

db = Database(database="Rel5", collection="books")
bookModel = BookModel(database=db)


bookCLI = BookCLI(bookModel)
bookCLI.run()
