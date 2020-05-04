from src import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    cpf = db.Column(db.String(11), nullable=False)

    endereco = db.relationship('Endereco', backref='usuario')
    telefones = db.relationship('Telefone', backref=db.backref('usuario', lazy=True))

    def __repr__(self):
        return f'Usuario {self.id_usuario}'


class Endereco(db.Model):
    __tablename__ = 'enderecos'

    id_endereco = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    complemento = db.Column(db.String(25), nullable=False)

    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)

    def __repr__(self):
        return f'<Endereco {self.cep}>'


class Telefone(db.Model):
    __tablename__ = 'telefones'

    id_telefone = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(11), nullable=False)

    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)

    def __repr__(self):
        return f'<Telefone {self.numero}>'
