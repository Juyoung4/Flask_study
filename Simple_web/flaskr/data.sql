--User 데이터 생성 (한 개 정도!)
INSERT INTO users(id, username, passwd) 
VALUES (null, 
        'test1',
        'test1password1'
);


--post 데이터 생성 (한 개 정도!)
INSERT INTO posts(id, writer_id, title, content)
VALUES (null,
        1,
        'blog title 1',
        'blog content 1'
);
