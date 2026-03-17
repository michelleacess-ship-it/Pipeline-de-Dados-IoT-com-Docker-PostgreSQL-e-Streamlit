CREATE VIEW avg_temp_por_dispositivo AS
SELECT 
device_id,
AVG(temperature) AS avg_temp
FROM temperature_readings
GROUP BY device_id;


CREATE VIEW leituras_por_hora AS
SELECT 
EXTRACT(HOUR FROM timestamp) AS hora,
COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora
ORDER BY hora;
