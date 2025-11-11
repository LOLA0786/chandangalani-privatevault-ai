if __name__ == "__main__":
    import os
    import sys
    import traceback

    try:
        port = int(os.environ.get("PORT", 10000))
        print(f"🚀 Starting Flask on port {port} ...")
        sys.stdout.flush()           # force log flush
        app.run(host="0.0.0.0", port=port)
    except Exception as e:
        print("🔥 ERROR during startup:", e)
        traceback.print_exc()
        sys.stdout.flush()
        open("render_crash.log", "w").write(traceback.format_exc())
