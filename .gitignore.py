for item in mis_tareas:
    lista.insert(tk.END, item["texto"])
    
    if item.get("completada", False):
      lista.itemconfig(tk.END, fg="gray")
    else:
      lista.itemconfig(tk.END, fg=item.get("color", "black"))