const apiBaseUrl = "http://localhost:8000/todos";
const todoTitleInput = document.getElementById("todo-title");
const todoDescriptionInput = document.getElementById("todo-description");
const addTodoButton = document.getElementById("add-todo-btn");
const todoList = document.getElementById("todo-list");

let isEditMode = false;
let editTodoId = null;

addTodoButton.addEventListener("click", async () => {
  const title = todoTitleInput.value;
  const description = todoDescriptionInput.value;

  if (title && description) {
    const todoData = {
      title: title,
      description: description,
    };

    if (isEditMode) {
      await fetch(`${apiBaseUrl}/${editTodoId}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(todoData),
      });
      isEditMode = false;
      editTodoId = null;
      addTodoButton.textContent = "Add Todo";
    } else {
      await fetch(apiBaseUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(todoData),
      });
    }
    todoTitleInput.value = "";
    todoDescriptionInput.value = "";
    fetchTodos();
  } else {
    alert("Please enter both title and description.");
  }
});
async function fetchTodos() {
  const response = await fetch(apiBaseUrl);
  const todos = await response.json();
  renderTodos(todos);
}
function renderTodos(todos) {
  todoList.innerHTML = "";

  todos.forEach((todo) => {
    const li = document.createElement("li");
    li.className = "todo-item";

    li.innerHTML = `
      <div>
        <span class="todo-title">${todo.title}</span>
        <p class="todo-description">${todo.description}</p>
      </div>
      <div class="todo-actions">
        <button onclick="editTodo(${todo.id}, '${todo.title}', '${todo.description}')">Edit</button>
        <button onclick="deleteTodo(${todo.id})">Delete</button>
      </div>
    `;
    todoList.appendChild(li);
  });
}

function editTodo(id, title, description) {
  todoTitleInput.value = title;
  todoDescriptionInput.value = description;
  isEditMode = true;
  editTodoId = id;
  addTodoButton.textContent = "Update Todo";
}
async function deleteTodo(id) {
  await fetch(`${apiBaseUrl}/${id}`, {
    method: "DELETE",
  });
  fetchTodos();
}
fetchTodos();
