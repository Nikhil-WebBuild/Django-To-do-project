# To-Do List Application

A simple Django web app to manage daily tasks with add, view, edit, and delete features.

## Features

-  **Create** Add new tasks with title, description, due date, and status
-  **Read** View all tasks in a clean list
-  **Update** Edit any task details
-  **Delete** Delete tasks after confirmation
-  **Status Tracking**: Track status: Pending, In Progress, Completed
-  **Modern UI** Colorful cards for each status
-  **Responsive Design** Works on phone and computer

## Installation & Setup

1. **Navigate to project directory:**
   ```bash
   Go to the project folder
   ```

2. **Run migrations (if needed):**
   ```bash
   python manage.py migrate
   ```

3. **Start the development server:**
   ```bash
   python manage.py runserver
   ```


## Usage

### How to Use
1. Add Task: Click "+ Add New Task", fill form, click "Add Task"
2. Edit Task: Click "Edit" on task card, change details, save
3. Delete Task: Click "Delete" on task card, confirm
4. Click " Add Task"


## Technologies Used

- **Backend**: Django 5.2
- **Frontend**: HTML5, CSS3
- **Database**: SQLite (default Django database)

## Design Features

- **Color-coded status**:
  -  Pending (Orange border)
  -  In Progress (Blue border)
  -  Completed (Green border)


## What i Learned
**This project shows**:
1. Django MVT (Model-View-Template)
2. Basic add/edit/delete/view operations
3. Reusable templates
4. Forms and styling
