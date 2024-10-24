from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)

# API để nhận dữ liệu từ client
@app.route('/predict', methods=['POST'])
def predict():
    # Lấy dữ liệu từ request
    data = request.json
    # Giả lập gọi model xử lý dữ liệu
    result = {"prediction": "result_from_model"}
    return jsonify(result)

# Chạy ứng dụng
if __name__ == '__main__':
    app.run(debug=True)
