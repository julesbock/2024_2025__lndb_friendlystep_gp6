from flask import Blueprint, session, request, jsonify
from main_tools import *

notifications_blueprint = Blueprint('notifications', __name__)
@notifications_blueprint.before_app_request
def before_request():
    if session.get('name_user'):
        current_notifications, nb_of_notif = get_user_notifications_under_thirty_min_and_nb_of_notif()
        if 'notifications' not in session:
            session['notifications'] = current_notifications
        if 'notification_count' not in session:
            session['notification_count'] = nb_of_notif
        if nb_of_notif > session['notification_count']:
            new_notifications = current_notifications[session['notification_count']:]
            session['notifications'].extend(new_notifications)
            session['notification_count'] = nb_of_notif
                            
@notifications_blueprint.route('/remove_notification', methods=['POST'])
def remove_notification():
    data = request.get_json()
    index = data.get('index')

    try:
        index = int(index)
    except (TypeError, ValueError):
        return jsonify({"status": "error", "message": "Invalid index"}), 400

    if 'notifications' in session:
        if 0 <= index < len(session['notifications']):
            session['notifications'].pop(index)
            session.modified = True
            return jsonify({"success": True}), 200

    return jsonify({"status": "error", "message": "Notification not found"}), 404




# Route pour vérifier s'il y a de nouvelles notifications
@notifications_blueprint.route('/check_for_new_notifications')
def check_for_new_notifications():
    if 'notifications' in session:
        # Charger les notifications actuelles depuis le JSON
        current_notifications, nb_of_notif = get_user_notifications_under_thirty_min_and_nb_of_notif()
        print(session['notifications'])
        # Si le nombre de notifications a changé, on retourne true
        if nb_of_notif > session['notification_count']:
            return jsonify({"new_notifications": True}), 200
    return jsonify({"new_notifications": False}), 200