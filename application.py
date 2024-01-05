
import app

app = app.create_app()

##开启debug模式可以热更新,host可以实现非127.0.0.1都可以访问

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=81)

