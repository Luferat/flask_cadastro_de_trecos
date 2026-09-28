-- Cria o banco de dados "database.db" --

-- 1) Apaga a tabela. CUIDADO! Só faça isso em desenvolvimento
DROP TABLE IF EXISTS thing;

-- 2) Cria a tabela "profile"
CREATE TABLE thing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    name TEXT,
	description TEXT,
    location TEXT, 
	photo TEXT,
	status TEXT CHECK (status IN ('on', 'off', 'del')) DEFAULT 'on'
);

-- 3) Cadastra alguns "profile" para experimentos iniciais
INSERT INTO thing 
( name, description, location, photo ) VALUES
( "Traquitana Junina", "Uma coisa que se acha por aí no período das festas juninas.", "Lá mesmo", "https://picsum.photos/400/300?random=1" ),
( "Peremboca quebrada", "Pedaço de alguma coisa, não se sabe de quê, mas é de origem terráquea.", "Encaixotado", "https://picsum.photos/400/300?random=2" ),
( "Lançador de sucata", "No melhor estilo 'arma infernal', mas não funciona mais. Se é que já funcionou.", "Bem perto", "https://picsum.photos/400/300?random=3" ),
( "Pescador de linha", "Usava quando era pequeno e não entendia pra que servia. Ainda não entendo.", "Por ai", "https://picsum.photos/400/300?random=4" );

INSERT INTO thing 
( name, description, location, photo ) VALUES
( "Traquitana Junina", "Uma coisa que se acha por aí no período das festas juninas.", "Lá mesmo", "https://picsum.photos/400/300?random=5" ),
( "Peremboca quebrada", "Pedaço de alguma coisa, não se sabe de quê, mas é de origem terráquea.", "Encaixotado", "https://picsum.photos/400/300?random=6" ),
( "Lançador de sucata", "No melhor estilo 'arma infernal', mas não funciona mais. Se é que já funcionou.", "Bem perto", "https://picsum.photos/400/300?random=7" ),
( "Pescador de linha", "Usava quando era pequeno e não entendia pra que servia. Ainda não entendo.", "Por ai", "https://picsum.photos/400/300?random=8" );

INSERT INTO thing 
( name, description, location, photo ) VALUES
( "Traquitana Junina", "Uma coisa que se acha por aí no período das festas juninas.", "Lá mesmo", "https://picsum.photos/400/300?random=9" ),
( "Peremboca quebrada", "Pedaço de alguma coisa, não se sabe de quê, mas é de origem terráquea.", "Encaixotado", "https://picsum.photos/400/300?random=10" ),
( "Lançador de sucata", "No melhor estilo 'arma infernal', mas não funciona mais. Se é que já funcionou.", "Bem perto", "https://picsum.photos/400/300?random=11" ),
( "Pescador de linha", "Usava quando era pequeno e não entendia pra que servia. Ainda não entendo.", "Por ai", "https://picsum.photos/400/300?random=12" );

INSERT INTO thing 
( name, description, location, photo ) VALUES
( "Traquitana Junina", "Uma coisa que se acha por aí no período das festas juninas.", "Lá mesmo", "https://picsum.photos/400/300?random=13" ),
( "Peremboca quebrada", "Pedaço de alguma coisa, não se sabe de quê, mas é de origem terráquea.", "Encaixotado", "https://picsum.photos/400/300?random=14" ),
( "Lançador de sucata", "No melhor estilo 'arma infernal', mas não funciona mais. Se é que já funcionou.", "Bem perto", "https://picsum.photos/400/300?random=15" ),
( "Pescador de linha", "Usava quando era pequeno e não entendia pra que servia. Ainda não entendo.", "Por ai", "https://picsum.photos/400/300?random=16" );

INSERT INTO thing 
( name, description, location, photo ) VALUES
( "Traquitana Junina", "Uma coisa que se acha por aí no período das festas juninas.", "Lá mesmo", "https://picsum.photos/400/300?random=17" ),
( "Peremboca quebrada", "Pedaço de alguma coisa, não se sabe de quê, mas é de origem terráquea.", "Encaixotado", "https://picsum.photos/400/300?random=18" ),
( "Lançador de sucata", "No melhor estilo 'arma infernal', mas não funciona mais. Se é que já funcionou.", "Bem perto", "https://picsum.photos/400/300?random=19" ),
( "Pescador de linha", "Usava quando era pequeno e não entendia pra que servia. Ainda não entendo.", "Por ai", "https://picsum.photos/400/300?random=20" );