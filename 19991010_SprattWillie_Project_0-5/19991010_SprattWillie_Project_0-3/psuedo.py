START

DEFINE FILENAME as 'allowed_vehicles.txt'

FUNCTION read_vehicles_from_file
    IF file FILENAME exists THEN
        OPEN FILENAME for reading
        READ all lines from FILENAME into list vehicles
        CLOSE file
    ELSE
        INITIALIZE vehicles with default list of authorized vehicles
        CALL write_vehicles_to_file with vehicles
    ENDIF
    RETURN vehicles
END FUNCTION

FUNCTION write_vehicles_to_file(vehicles)
    OPEN FILENAME for writing
    FOR each vehicle in vehicles DO
        WRITE vehicle to FILENAME
    ENDFOR
    CLOSE file
END FUNCTION

FUNCTION onLoad
    CALL read_vehicles_from_file
    STORE result in AllowedVehiclesList

    DISPLAY menu and get user input into execution

    IF execution equals 1 THEN
        DISPLAY authorized vehicles from AllowedVehiclesList
        CALL onLoad

    ELSE IF execution equals 2 THEN
        DISPLAY prompt for vehicle name input into search
        IF search in AllowedVehiclesList THEN
            DISPLAY vehicle is authorized message
        ELSE
            DISPLAY vehicle is not authorized message
        ENDIF
        CALL onLoad

    ELSE IF execution equals 3 THEN
        DISPLAY prompt for new vehicle input into new_add
        ADD new_add to AllowedVehiclesList
        CALL write_vehicles_to_file with AllowedVehiclesList
        DISPLAY vehicle added message
        CALL onLoad

    ELSE IF execution equals 4 THEN
        DISPLAY prompt for vehicle name to remove input into new_delete
        DISPLAY confirmation prompt into assurance
        IF assurance equals "yes" THEN
            IF new_delete in AllowedVehiclesList THEN
                REMOVE new_delete from AllowedVehiclesList
                CALL write_vehicles_to_file with AllowedVehiclesList
                DISPLAY vehicle removed message
            ELSE
                DISPLAY vehicle not found message
            ENDIF
        ENDIF
        CALL onLoad

    ELSE IF execution equals 5 THEN
        DISPLAY goodbye message

    ELSE
        DISPLAY invalid option message
        CALL onLoad
    ENDIF
END FUNCTION

CALL onLoad

END
