from flask import jsonify


def json_response(data=None):
    if data and isinstance(data, list) and len(data):
        data = list(map(lambda row: row._asdict(), data))
        return jsonify({
            'success': True,
            'data': data
        })
    return jsonify({
        'success': False,
        'data': []
    })
