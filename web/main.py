from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # アップロードされたファイルを取得
        uploaded_file = request.files['file']

        if uploaded_file:
            # 画像を保存するディレクトリ（staticディレクトリ内に保存する例）
            upload_folder = 'img/before'
            uploaded_file.save(f'{upload_folder}/{uploaded_file.filename}')

            # アップロードが完了したメッセージを表示
            message = 'アップロードが完了しました！'
            return render_template('newacount.html', message=message)

    return render_template('index.html', message=None)

if __name__ == '__main__':
    app.run(debug=True)
