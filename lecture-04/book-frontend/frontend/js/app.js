// Endereço da sua API — muda se precisar
const API = "http://localhost:8000";

// ─── GET /books ───────────────────────────────────────────
// Carrega os livros e renderiza na tela
// Se "read" for passado, filtra: ?read=true ou ?read=false
async function loadBooks(read = null) {
  let url = `${API}/books`;

  // Monta a query param se o filtro foi passado
  if (read !== null) {
    url += `?read=${read}`;
  }

  const response = await fetch(url);
  const books = await response.json();

  renderBooks(books);
}

// ─── POST /books ──────────────────────────────────────────
// Pega os dados do formulário e cria um livro novo
document.getElementById("book-form").addEventListener("submit", async (e) => {
  e.preventDefault(); // impede o form de recarregar a página

  const body = {
    title: document.getElementById("title").value,
    author: document.getElementById("author").value,
    read: document.getElementById("read").checked,
  };

  await fetch(`${API}/books`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body), // converte objeto JS pra JSON
  });

  e.target.reset(); // limpa o formulário
  loadBooks();      // recarrega a lista
});

// ─── DELETE /books/{id} ───────────────────────────────────
async function deleteBook(id) {
  await fetch(`${API}/books/${id}`, { method: "DELETE" });
  loadBooks(); // recarrega depois de deletar
}

// ─── Renderizar os livros na tela ─────────────────────────
function renderBooks(books) {
  const list = document.getElementById("book-list");

  if (books.length === 0) {
    list.innerHTML = "<p>Nenhum livro encontrado.</p>";
    return;
  }

  // Cria um card pra cada livro
  list.innerHTML = books.map(book => `
    <div class="book-card">
      <div class="book-info">
        <div class="book-title">${book.title}</div>
        <div class="book-author">${book.author}</div>
      </div>
      <div style="display:flex; align-items:center; gap:0.5rem">
        <span class="book-status ${book.read ? 'lido' : ''}">
          ${book.read ? "lido" : "não lido"}
        </span>
        <button class="delete-btn" onclick="deleteBook(${book.id})">deletar</button>
      </div>
    </div>
  `).join("");
}

// Carrega os livros quando a página abre
loadBooks();
