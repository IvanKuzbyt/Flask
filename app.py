from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список для зберігання записів блогу
posts = []

# Маршрут для перегляду списку записів
@app.route('/')
@app.route('/posts')
def post_list():
    return render_template('tasks.html', posts=posts)

# Маршрут для додавання нового запису
@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if title and content:
            posts.append({'title': title, 'content': content})
            return redirect(url_for('post_list'))
        else:
            return "Заголовок і вміст не можуть бути порожніми", 400
    return render_template('add_task.html')

# Маршрут для редагування запису
@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    if post_id >= len(posts):
        return "Запис не знайдено", 404
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if title and content:
            posts[post_id] = {'title': title, 'content': content}
            return redirect(url_for('post_list'))
        else:
            return "Заголовок і вміст не можуть бути порожніми", 400
    return render_template('add_task.html', post=posts[post_id])

# Маршрут для видалення запису
@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    if post_id >= len(posts):
        return "Запис не знайдено", 404
    posts.pop(post_id)
    return redirect(url_for('post_list'))

# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True)
