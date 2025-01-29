function addTask(taskType) {
    // Afficher la fenêtre modale pour entrer les informations de la tâche
    document.getElementById("task-modal").classList.add("show");
    document.getElementById("task-type").value = taskType;
}

function closeModal() {
    document.getElementById("task-modal").classList.remove("show");
    // Réinitialiser les champs de saisie
    document.getElementById("task-title").value = '';
    document.getElementById("task-description").value = '';
}

function saveTaskDetails() {
    let title = document.getElementById("task-title").value;
    let description = document.getElementById("task-description").value;
    let taskType = document.getElementById("task-type").value;

    if (!title || !description) {
        alert("Tous les champs doivent être remplis.");
        return;
    }

    // Créer un nouvel élément pour afficher la tâche
    let taskContainer = document.createElement("div");
    taskContainer.classList.add("task-block");
    
    let descriptionContainer = document.createElement("div");
    descriptionContainer.classList.add("task-description");
    descriptionContainer.textContent = description;

    let deleteButton = document.createElement("button");
    deleteButton.textContent = "Supprimer";
    deleteButton.classList.add("delete-button");
    deleteButton.onclick = () => {
        deleteTask('app1-', taskType, task);
        taskContainer.remove();
    };

    taskContainer.innerHTML = `<h3>${title}</h3>`;
    taskContainer.appendChild(descriptionContainer);
    taskContainer.appendChild(deleteButton);

    // Clic pour afficher/masquer la description
    taskContainer.addEventListener('click', () => {
        descriptionContainer.classList.toggle('visible');
    });

    document.getElementById(`${taskType}-tasks-list`).appendChild(taskContainer);

    // Sauvegarder dans le LocalStorage
    let taskData = { title, description };
    saveTask('app1-', taskType, taskData);

    // Fermer le modal
    closeModal();
    location.reload();
}

function saveTask(appPrefix, taskType, taskData) {
    let tasks = JSON.parse(localStorage.getItem(appPrefix + taskType)) || [];
    tasks.push(taskData);
    localStorage.setItem(appPrefix + taskType, JSON.stringify(tasks));
}

function deleteTask(appPrefix, taskType, taskData) {
    let tasks = JSON.parse(localStorage.getItem(appPrefix + taskType)) || [];
    tasks = tasks.filter(task => task.title !== taskData.title || task.description !== taskData.description);
    localStorage.setItem(appPrefix + taskType, JSON.stringify(tasks));
}

document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.getElementById("task-sidebar");
    const closeSidebar = document.getElementById("close-sidebar");

    function closeSidebarFunction() {
        sidebar.classList.remove("visible");
    }

    // Associer la fonction de fermeture au clic sur le bouton de fermeture
    closeSidebar.addEventListener("click", closeSidebarFunction);
});

function showTaskDetails(title, description) {
    document.getElementById("sidebar-title").textContent = title;
    document.getElementById("sidebar-description").textContent = description;
    document.getElementById("task-sidebar").classList.add("visible");
}

function loadTasks() {
    ["daily", "weekly", "monthly"].forEach(taskType => {
        let tasks = JSON.parse(localStorage.getItem('app1-' + taskType)) || [];
        tasks.forEach(task => {
            let taskContainer = document.createElement("div");
            taskContainer.classList.add("task-block");
            
            let descriptionContainer = document.createElement("div");
            descriptionContainer.classList.add("task-description");
            descriptionContainer.textContent = task.description;
            
            let deleteButton = document.createElement("button");
            deleteButton.textContent = "Supprimer";
            deleteButton.classList.add("delete-button");
            deleteButton.onclick = () => {
                deleteTask('app1-', taskType, task);
                taskContainer.remove();
            };
            
            taskContainer.innerHTML = `<h3>${task.title}</h3>`;
            taskContainer.appendChild(deleteButton);

            // 📌 Afficher la description dans la sidebar au clic
            taskContainer.addEventListener('click', () => {
                showTaskDetails(task.title, task.description);
            });

            document.getElementById(`${taskType}-tasks-list`).appendChild(taskContainer);
        });
    });
}

document.addEventListener("DOMContentLoaded", loadTasks);