from photolog import create_app

applilcation = create_app()

if __name__ == '__main__':
    print ("starting test server...")

    application.run(host='0.0.0.0' , port = 5000, debug = True)

