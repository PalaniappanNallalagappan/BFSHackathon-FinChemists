CREATE DEFINER=`root`@`localhost` PROCEDURE `ServiceRequestsPopulate`()
BEGIN
	DECLARE l_finished INTEGER DEFAULT 0;
	DECLARE l_email_id INTEGER(11);
	DECLARE l_email_textmessage VARCHAR(8000);
	DECLARE l_email_cat VARCHAR(256);
	DECLARE l_email_dt DATETIME;
    
    DECLARE l_seq INTEGER(10);
   
	DECLARE cur_sr CURSOR
	FOR
	SELECT id, textmessage, category, date FROM banking.emails;

	DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET l_finished = 1;
	
    SET l_seq = 1000;
    
	OPEN cur_sr;
	REPEAT
		FETCH cur_sr INTO l_email_id, l_email_textmessage, l_email_cat, l_email_dt;
		
        IF NOT l_finished THEN
			#SELECT l_email_id, l_email_textmessage, l_email_cat, l_email_dt;
        
			INSERT INTO banking.requests(srid,textmessage,assignedto,date,status)
			VALUES (l_seq,l_email_textmessage,l_email_cat,l_email_dt,'New');
            
            SET l_seq = l_seq + 1; 
            
		END IF;
   
	UNTIL l_finished END REPEAT;
		
	CLOSE cur_sr;
    
    COMMIT;
    
UPDATE banking.requests 
SET 
    assignedto = CASE
        WHEN assignedto = '\'Personal_Info_Update\'' THEN 'Personal Info Update Department'
        WHEN assignedto = '\'Supplementary_Card_Update\'' THEN 'Supplementary Department'
        WHEN assignedto = '\'FollowUp_Personal_Info_Update\'' THEN 'Escalation Department'
        WHEN assignedto = '\'Complaints_Personal_Info_Update\'' THEN 'Complaints Department'
        WHEN assignedto = '\'Urgent_Personal_Info_Update\'' THEN 'High Priority Department'
        WHEN assignedto = '\'Social_Media_Complaints_Personal_Info_Update\'' THEN 'Social Media Department'
        ELSE assignedto
    END;

	COMMIT;
    
	UPDATE banking.requests 
SET 
    status = 'WIP'
WHERE
    assignedto = 'Escalation Department';
    
    
	UPDATE banking.requests 
SET 
    status = 'WIP'
WHERE
    assignedto = 'Complaints Department';
     
    COMMIT;

END