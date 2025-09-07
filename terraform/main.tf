// Configuração do provedor de nuvem (simulando AWS)
provider "aws" {
  region = "us-east-1"
}

// SIMULAÇÃO: Grupo de Segurança (Firewall)
// Permite tráfego na porta 8501 (Streamlit) e 22 (SSH para acesso)
resource "aws_security_group" "agent_sg" {
  name        = "agent-security-group"
  description = "Allow web and SSH traffic"

  ingress {
    from_port   = 8501
    to_port     = 8501
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] // Em produção, restrinja ao seu IP
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

// SIMULAÇÃO: Instância de Servidor (EC2)
// Máquina virtual onde o container Docker do agente seria executado
resource "aws_instance" "agent_server" {
  ami           = "ami-0c55b159cbfafe1f0" // Exemplo de AMI para Amazon Linux 2
  instance_type = "t2.micro"              // Tipo de instância de baixo custo

  vpc_security_group_ids = [aws_security_group.agent_sg.id]

  // Script de inicialização que seria executado ao criar a instância
  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo yum install -y docker
              sudo service docker start
              sudo usermod -a -G docker ec2-user
              # Comando para baixar e rodar a imagem Docker do agente (a imagem precisaria estar em um registro como o Docker Hub)
              # docker run -d -p 8501:8501 seu-usuario/pyunit-scribe:latest
              EOF

  tags = {
    Name = "IA-Agent-Server"
  }
}

// SIMULAÇÃO: Saída com o IP público do servidor
// Após o provisionamento, o Terraform mostraria o IP para acessar o agente
output "agent_public_ip" {
  value = aws_instance.agent_server.public_ip
}