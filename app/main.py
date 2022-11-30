from setup import app

if __name__ == '__main__':
  try:
    app.run(debug=True)
  except KeyboardInterrupt:
    print("keyboard interrupt detected")
