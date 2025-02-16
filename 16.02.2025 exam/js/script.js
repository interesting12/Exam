class Book {
    constructor (id, title, author){
        this.id = id;
        this.title = title;
        this.author = author;
        this.read = false;

    }

}

const books = [
    new Book(1, "1984", "George Orwell", ),
    new Book(2, "The Master and Margarita", "Mikhail Bulgakov",  ),
    new Book(3, "Crime and Punishment", "Fyodor Dostoevsky" )

];
function renderBooks () {
    const bookList = document.getElementById("book-list");
    bookList.innerHTML = "";
    books.forEach(book => {
        const bookCard = document.createElement("div");
        bookCard.classList.add("book-card");
        bookCard.innerHTML = `
        <h3>${book.title}</h3>
        <p>${book.author}</p>
        <button onclick="addToLibrary(${book.id})">Add To Library</button>
        `;
        bookList.appendChild(bookCard);

    });

}
function addToLibrary(id){
    let library= JSON.parse(localStorage.getItem('library')) ||[];
    const bookToAdd = books.find(book => book.id === id);
    if(!library.some(book => book.id === id)) {
        library.push(bookToAdd);
        localStorage.setItem('library', JSON.stringify(libraryList));
    }

}

document.addEventListener("DOMContentLoaded", renderBooks);
