# imports flask, render_template, request, url_for, redirect which is needed for app to work
from flask import Flask, render_template, request, url_for, redirect
# imports socketio, emit fra flask_socketio
from flask_socketio import SocketIO, emit

# to make app easier to code
app = Flask(__name__)

# makes a seceret key for the config
app.config[ 'SECRET_KEY' ] = 'bGFnZXRhdnNhbXVlbA=='
# to make app easier to code
socketio = SocketIO( app )

# app.route says which html5 document to render
@app.route( '/' )
def hello():
# chooses the file
  return render_template( './secret.html' )

# displays message info to console
def messageRecived():
  print( 'message was received!!!' )

# more console info
@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )

# I use this so that the passcode can redirect to the porpper html5 file for the actuall app.
@app.route('/mess', methods=['GET', 'POST'])
def mess():
    if request.method == 'POST':

        return redirect(url_for('index'))

    return render_template('mess.html')


# necessity
if __name__ == '__main__':
  socketio.run( app, debug = True )