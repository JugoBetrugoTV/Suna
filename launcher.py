"""HOLLOWMERE - Standalone Launcher
Opens the game HTML in a borderless webview window.
Used by PyInstaller to create HOLLOWMERE.exe
"""
import http.server
import threading
import webbrowser
import os
import sys
import socket


def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]


def get_html_path():
    if getattr(sys, '_MEIPASS', None):
        return os.path.join(sys._MEIPASS, 'HOLLOWMERE.html')
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'HOLLOWMERE.html')


def main():
    html_path = get_html_path()
    if not os.path.exists(html_path):
        print(f"FEHLER: {html_path} nicht gefunden!")
        input("Druecke ENTER...")
        return

    serve_dir = os.path.dirname(html_path)
    port = find_free_port()

    handler = lambda *args: http.server.SimpleHTTPRequestHandler(*args, directory=serve_dir)
    server = http.server.HTTPServer(('127.0.0.1', port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    url = f'http://127.0.0.1:{port}/HOLLOWMERE.html'

    # Try webview library first (proper window), fall back to browser
    try:
        import webview
        webview.create_window('HOLLOWMERE', url, width=1024, height=768,
                              background_color='#000000', text_select=False)
        webview.start()
    except ImportError:
        print(f"Oeffne Spiel im Browser: {url}")
        print("Fenster offen lassen! Schliessen beendet das Spiel.")
        webbrowser.open(url)
        try:
            input("\nDruecke ENTER um das Spiel zu beenden...\n")
        except KeyboardInterrupt:
            pass

    server.shutdown()


if __name__ == '__main__':
    main()
