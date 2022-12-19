
const choices = () => {

    var dataSource = document.getElementById("data_source")
    var activity = document.getElementById("activity")
    var viewMode = document.getElementById("view_mode")
    var selectMetaTable = document.getElementById("select_meta_table")
    var update = document.getElementById("update")
    var tableId = document.getElementById("table_id")
    var tableName = document.getElementById("table_name")
    var submit = document.getElementById("submit")

    if (!dataSource.value) {
        submit.disabled = true;
    } else {
        if (activity.value) {
            
            switch (activity.value) {
                case 'VALL':
                    viewMode.disabled = false;
                    submit.disabled = false;
                    selectMetaTable.disabled = true;
                    update.disabled = true;
                    tableId.disabled = true;
                    tableName.disabled = true;
                    break;
                
                case 'VMT':
                    selectMetaTable.disabled = false;
                    submit.disabled = false;
                    viewMode.disabled = true;
                    update.disabled = true;
                    tableId.disabled = true;
                    tableName.disabled = true;
                    break;
            
                case 'VDT':
                    update.disabled = false;
                    tableId.disabled = false;
                    tableName.disabled = false;
                    submit.disabled = false;
                    viewMode.disabled = true;
                    selectMetaTable.disabled = true;
                    break;
            
                default:
                    viewMode.disabled = true;
                    submit.disabled = true;
                    selectMetaTable.disabled = true;
                    update.disabled = true;
                    tableId.disabled = true;
                    tableName.disabled = true;
                    break;
            }

        }

    }

}