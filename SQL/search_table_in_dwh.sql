SELECT DatabaseName, TABLENAME, ColumnName
FROM dbc.ColumnsV
WHERE DatabaseName LIKE 'P_ATA%' AND ColumnName = 'dealer_id'
--WHERE DatabaseName LIKE ANY ('P_ATA%','%D_ATA%') AND ColumnName IN ('dealer_id','dealer_id_long')
ORDER BY 1,2,3

--HELP TABLE P_ATA_MV_TNPS.VWL_Add_Question 
