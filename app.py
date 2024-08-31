from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

 
@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)



@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        save_task(task)
    return redirect(url_for('index'))


def save_task(task):
    with open('tasks.txt', 'a') as f:
        f.write(task + '\n')




def load_tasks():
    try:
        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()
            tasks = [task.strip() for task in tasks]
    except FileNotFoundError:
        tasks = []
    return tasks





@app.route('/remove/<task>')
def remove_task(task):
    tasks = load_tasks()
    tasks = [t for t in tasks if t != task]
    with open('tasks.txt', 'w') as f:
        for t in tasks:
            f.write(t + '\n')
    return redirect(url_for('index'))



@app.route('/clear')
def clear_tasks():
    with open('tasks.txt', 'w'):
        pass   
    return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(debug=True)
