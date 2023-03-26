from flask import Flask, render_template,request


app = Flask(__name__)


@app.route('/')
def Home():
    """opens up a default page displaying file1"""

    with open(f"Python_test_jr/file1.txt", encoding='utf-8') as file:
        save_data = file.readlines()
    return render_template("display.html", quotes=save_data)


@app.route('/file<int:num>', methods=['GET'])
def read_files(num):
    """Takes a mandatory parameter num and displays all
    files upon calling, viz. num=1,2,3 or 4.
    Also reads a set of lines when
    optional parameters n1 and n2 are given.
    When no parameter is given it reads the entire lines"""

    # optional parameters
    n1 = request.args.get('n1')
    n2 = request.args.get('n2')

    save_data = []
    with open(f"Python_test_jr/file{num}.txt", encoding='utf8') as file:
        data_list = file.readlines()
        try:
            for i in range(int(n1), int(n2) + 1):
                save_data.append(data_list[i])

        # upon any exception read the entire page and prints the error message.
        # However, when Index error is there, it displays error message on web page
        except TypeError as error_message:
            print(f"The error is : {error_message}")
            save_data = data_list

        except IndexError as error_message:
            print(f"The error is : {error_message}")
            save_data = data_list
            return f"The error is : {error_message}"

        except ValueError as error_message:
            print(f"The error is : {error_message}")
            save_data = data_list


    return render_template("display.html", quotes=save_data)


if __name__ == "__main__":
    app.run(debug=True)
