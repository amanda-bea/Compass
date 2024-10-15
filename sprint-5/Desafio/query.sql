SELECT 
    CAST(MAX(
        CASE 
            WHEN datachegada LIKE '%/%' THEN 
                CAST(SUBSTRING(datachegada, 7) AS INT)
            ELSE 
                CAST(SUBSTRING(datachegada, 1, 4) AS INT)
        END
    ) AS INT) - 
    CAST(MIN(
        CASE 
            WHEN datachegada LIKE '%/%' THEN 
                CAST(SUBSTRING(datachegada, 7) AS INT)
            ELSE 
                CAST(SUBSTRING(datachegada, 1, 4) AS INT)
        END
    ) AS INT) AS diferenca_anos
FROM S3Object
WHERE Sobrenome = 'de Jesus' OR Sobrenome = 'de Carvalho' OR Sobrenome = 'Carvalho' OR Sobrenome = 'Marques'