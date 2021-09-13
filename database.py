import sqlite3

from dataclasses import dataclass


@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''


class Database:
    def __init__(self, nome):
        self.nome = f'{nome}.db'
        self.conn = sqlite3.connect(self.nome)
        self.note = self.conn.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title STRING, content TEXT NOT NULL); ")

    def add(self, note):
        self.note = self.conn.execute(f"INSERT INTO note(title, content) VALUES('{note.title}','{note.content}') ")
        self.conn.commit

    def get_all(self):
        notes = self.conn.execute("SELECT id, title, content FROM note")
        lista_anotacoes = []
        for linha in notes:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            note = Note(id, title, content)
            lista_anotacoes.append(note)
        return lista_anotacoes

    def update(self, entry):
        self.note = self.conn.execute(f'UPDATE note SET title = {entry.title}, content = {entry.content} WHERE id = {entry.id};')
        self.conn.commit()

    def delete(self, note_id):
        self.note = self.conn.execute(f'DELETE FROM  note WHERE  id = {note_id};')
        self.conn.commit()