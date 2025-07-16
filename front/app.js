let token = null;

async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();
        if (response.ok) {
            token = data.token;
            document.getElementById('login-section').style.display = 'none';
            document.getElementById('app-content').style.display = 'block';
            loadTasks();
        } else {
            alert(data.error || 'Login failed');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}


async function loadTasks() {
    try {
        const status = document.getElementById('status-filter').value;
        let url = '/tasks';
        if (status) {
            url += `?status=${encodeURIComponent(status)}`;
        }
        const response = await fetch(url, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        const data = await response.json();
        renderTasks(data.tasks);
    } catch (error) {
        console.error('Error loading tasks:', error);
    }
}




function renderTasks(tasks) {
    const container = document.getElementById('tasks-container');
    container.innerHTML = '';

    tasks.forEach(task => {
        
        let borderColor = '';
        if (task.status === 'In Progress') {
            borderColor = 'yellow';
        } else if (task.status === 'Completed') {
            borderColor = 'green';  
            borderColor = 'gray';  
        }

        const taskElement = document.createElement('div');
        taskElement.className = 'task';
        taskElement.style.border = `2px solid ${borderColor}`;
        taskElement.innerHTML = `
            <h3>${task.title}</h3>
            <p>${task.description}</p>
            <p>Status: ${task.status}</p>
            <button onclick="progressTask(${task.id})">Progress</button>
           
            <button onclick="completeTask(${task.id})">Complete</button>
            <button onclick="deleteTask(${task.id})">Delete</button>
        `;
        container.appendChild(taskElement);
    });
}


async function addTask() {
    const title = document.getElementById('task-title').value;
    const description = document.getElementById('task-desc').value;

    try {
        const response = await fetch('/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ title, description })
        });

        if (response.ok) {
            document.getElementById('task-title').value = '';
            document.getElementById('task-desc').value = '';
            loadTasks();
        }
    } catch (error) {
        console.error('Error adding task:', error);
    }
}



async function progressTask(taskId) {
    try {
        await fetch(`/tasks/${taskId}/progress`, {
            method: 'PUT',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        loadTasks();
    } catch (error) {
        console.error('Error progressing task:', error);
    }
}


async function completeTask(taskId) {
    try {
        await fetch(`/tasks/${taskId}/complete`, {
            method: 'PUT',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        loadTasks();
    } catch (error) {
        console.error('Error completing task:', error);
    }
}

async function deleteTask(taskId) {
    try {
        await fetch(`/tasks/${taskId}`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        loadTasks();
    } catch (error) {
        console.error('Error deleting task:', error);
    }
}

document.getElementById('show-register-btn').onclick = () => {
    document.getElementById('register-modal').style.display = 'flex';
};
document.getElementById('register-cancel-btn').onclick = () => {
    document.getElementById('register-modal').style.display = 'none';
};
document.getElementById('register-submit-btn').onclick = async () => {
    const first_name = document.getElementById('reg-first-name').value.trim();
    const last_name = document.getElementById('reg-last-name').value.trim();
    const username = document.getElementById('reg-username').value.trim();
    const password = document.getElementById('reg-password').value;

    if (!first_name || !username || !password) {
        alert('Please fill in all required fields.');
        return;
    }

    try {
        const response = await fetch('/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ first_name, last_name, username, password })
        });

        const data = await response.json();

        if (response.ok) {
            alert('Successfully registered new user!');
            document.getElementById('register-modal').style.display = 'none';
            document.getElementById('reg-first-name').value = '';
            document.getElementById('reg-last-name').value = '';
            document.getElementById('reg-username').value = '';
            document.getElementById('reg-password').value = '';
        } else {
            alert(data.error || 'Registration failed');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Registration failed due to network error');
    }
};
