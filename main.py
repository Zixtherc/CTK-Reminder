import modules

if __name__ == "__main__":
    try:
        modules.app.mainloop()
    except KeyboardInterrupt:
        print("Shutting down")