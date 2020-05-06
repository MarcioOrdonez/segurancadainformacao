from src import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    funcionario = db.Column(db.Boolean, nullable=False)

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


class Servicos(db.Model):
    __tablename__ = 'servicos'

    id_servico = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    descricao = db.Column(db.String(60), nullable=False)
    preco = db.Column(db.String(60), nullable=False)
    duracao = db.Column(db.String(60), nullable=False)


class Agendamento(db.Model):
    __tablename__ = 'agendamento'

    id_agendamento = db.Column(db.Integer, primary_key=True)

    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_servico = db.Column(db.Integer, db.ForeignKey('servicos.id_servico'), nullable=False)

class Agenda(db.Model):
    __tablename__ = 'agenda'

    id = db.Column(db.Integer, primary_key=True)
    data_agendada = db.Column(db.DateTime, nullable=False)
    id_agendamento = db.Column(db.Integer, db.ForeignKey('agendamento.id_agendamento'), nullable=False)