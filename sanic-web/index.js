$(function () {
    $(".field").hide();
    $("#result").hide();
    $("#display-field").show();

    $("#sidebar .query-all-device").off("click").on("click",function(){
        only_show("display-field");
        get_all_device();
    });

    $("#sidebar .query-all-device-and-group").off("click").on("click",function(){
        only_show("display-field");
        get_all_device_and_group();
    });

    $("#sidebar .query-all-group").off("click").on("click",function(){
        only_show("display-field");
        get_all_group();
    });

    $("#sidebar .get-device-and-group-by-id").off("click").on("click",function(){
        $(".field").hide();
        $("#get-device-and-group-by-id-field").show();
        $("#get-device-and-group-by-id-field .btn").off("click").on("click",function(){
            only_show("display-field")
            get_device_and_group_by_id();
        });
    });

    $("#sidebar .delete-device-by-id").off("click").on("click",function(){
        $(".field").hide();
        $("#delete-device-by-id-field").show();
        $("#delete-device-by-id-field .btn").off("click").on("click",function(){
            only_show("display-field")
            delete_device_by_id();
        });
    });

    $("#sidebar .delete-relation-by-id").off("click").on("click",function(){
        $(".field").hide();
        $("#delete-relation-by-id-field").show();
        $("#delete-relation-by-id-field .btn").off("click").on("click",function(){
            only_show("display-field")
            delete_relation_by_id();
        });
    });

    $("#sidebar .delete-group-by-num").off("click").on("click",function(){
        $(".field").hide();
        $("#delete-group-by-num-field").show();
        $("#delete-group-by-num-field .btn").off("click").on("click",function(){
            only_show("display-field")
            delete_group_by_number();
        });
    });

    $("#sidebar .get-device-by-group").off("click").on("click",function(){
        $(".field").hide();
        $("#get-device-by-group-field").show();
        $("#get-device-by-group-field .btn").off("click").on("click",function(){
            only_show("display-field")
            get_device_by_group();
        });
    });

    $("#sidebar .register-device").off("click").on("click",function(){
        $(".field").hide();
        $("#register-field").show();
        $("#register-field .btn").off("click").on("click",function(){
            only_show("display-field")
            register_device();
        });
    });

    $("#sidebar .device-login").off("click").on("click",function(){
        $(".field").hide();
        $("#device-login-field").show();
        $("#device-login-field .btn").off("click").on("click",function(){
            only_show("display-field")
            device_login();
        });
    });

    $("#sidebar .database-logging-query").off("click").on("click",function(){
        only_show("display-field");
        logging_query(1);
    });

    $("#sidebar .device-logging-query").off("click").on("click",function(){
        only_show("display-field");
        logging_query(2);
    });

    $("#sidebar .status-logging-query").off("click").on("click",function(){
        only_show("display-field");
        logging_query(3);
    });

    $("#sidebar .add-group").off("click").on("click",function(){
        $(".field").hide();
        $("#add-group-field").show();
        $("#add-group-field .btn").off("click").on("click",function(){
            only_show("display-field")
            add_group();
        });
    });

    $("#sidebar .add-relation").off("click").on("click",function(){
        $(".field").hide();
        $("#add-relation-field").show();
        $("#add-relation-field .btn").off("click").on("click",function(){
            only_show("display-field")
            add_relation();
        });
    });

    function get_all_device() {
        $.ajax({
            url: 'http://8.137.97.80/north/get',
            type: 'post',
            dataType: "json",
            data: '{"method": "get_all_device","data": []}',
            cache: false,
            headers: {
                'dataType': 'json',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'x-requested-with': 'XMLHttpRequest',
                'Cache-Control': 'max-age=0',
                'Pragma': 'no-cache',
                'Content-Type': 'application/json',
            },
            success: function (res) {
                if (res.result == true) {
                    $('#result').html(syntaxHighlight(res.data[0]));
                    for (var i = 1; i < res.data.length; ++i){
                        $('#result').append("<br><br>");
                        $('#result').append(syntaxHighlight(res.data[i]));
                    }
                } else {
                    $('#result').html(syntaxHighlight(res));
                }
            },
            error: function (e) {
                alert_error();
            }
        });
    }

    function get_all_device_and_group() {
        $.ajax({
            url: 'http://8.137.97.80/north/get',
            type: 'post',
            dataType: "json",
            data: '{"method": "get_all_device_and_group","data": []}',
            cache: false,
            headers: {
                'dataType': 'json',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'x-requested-with': 'XMLHttpRequest',
                'Cache-Control': 'max-age=0',
                'Pragma': 'no-cache',
                'Content-Type': 'application/json',
            },
            success: function (res) {
                if (res.result == true) {
                    $('#result').html(syntaxHighlight(res.data[0]));
                    for (var i = 1; i < res.data.length; ++i){
                        $('#result').append("<br><br>");
                        $('#result').append(syntaxHighlight(res.data[i]));
                    }
                } else {
                    $('#result').html(syntaxHighlight(res));
                }
            },
            error: function (e) {
                alert_error();
            }
        });
    }

    function get_all_group() {
        $.ajax({
            url: 'http://8.137.97.80/north/get',
            type: 'post',
            dataType: "json",
            data: '{"method": "get_all_group","data": []}',
            cache: false,
            headers: {
                'dataType': 'json',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'x-requested-with': 'XMLHttpRequest',
                'Cache-Control': 'max-age=0',
                'Pragma': 'no-cache',
                'Content-Type': 'application/json',
            },
            success: function (res) {
                if (res.result == true) {
                    $('#result').html(syntaxHighlight(res.data[0]));
                    for (var i = 1; i < res.data.length; ++i){
                        $('#result').append("<br><br>");
                        $('#result').append(syntaxHighlight(res.data[i]));
                    }
                } else {
                    $('#result').append(syntaxHighlight(res));
                }
            },
            error: function (e) {
                alert_error();
            }
        });
    }

    function register_device() {

        var json = {
            "method": "register_device",
            "data": [
                {
                    "name": $("#register-field #name").val(),
                    "type": $("#register-field #type").val(),
                    "state": $("#register-field #state").val(),
                    "hardware": {
                        "sn": $("#register-field #hardware-sn").val(),
                        "model": $("#register-field #hardware-model").val(),
                    },
                    "software": {
                        "base": {
                            "version": $("#register-field #software-base-version").val(),
                            "lastUpdate": $("#register-field #software-base-lastUpdate").val(),
                            "status": $("#register-field #software-base-status").val()
                        },
                        "work": {
                            "version": $("#register-field #software-work-version").val(),
                            "lastUpdate": $("#register-field #software-work-lastUpdate").val(),
                            "status": $("#register-field #software-work-status").val()
                        }
                    },
                    "nic": {
                        "eth": {
                            "mac": $("#register-field #nic-eth-mac").val(),
                            "ipv4": $("#register-field #nic-eth-ipv4").val()
                        },
                        "wifi": {
                            "mac": $("#register-field #nic-wifi-mac").val(),
                            "ipv4": $("#register-field #nic-wifi-ipv4").val()
                        }
                    },
                    "LTE_IMEI": $("#register-field #lte-imei").val()
                }
            ]
        };

        $.ajax({
            url: 'http://8.137.97.80/north/register',
            type: 'post',
            dataType: "json",
            data: JSON.stringify(json),
            cache: false,
            headers: {
                'dataType': 'json',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'x-requested-with': 'XMLHttpRequest',
                'Cache-Control': 'max-age=0',
                'Pragma': 'no-cache',
                'Content-Type': 'application/json',
            },
            success: function (res) {
                if (res.result == true) {
                    $('#result').html(syntaxHighlight(res.data));
                } else {
                    $('#result').html(syntaxHighlight(res));
                }
            },
            error: function (e) {
                alert_error();
            }
        });
    }

    function device_login() {
        var json = {
            "id": $("#device-login-field #device-login-id").val(),
            "password": $("#device-login-field #device-login-pwd").val()
        }

        $.ajax({
            url: 'http://8.137.97.80/south/auth',
            type: 'post',
            dataType: "json",
            data: JSON.stringify(json),
            cache: false,
            headers: {
                'dataType': 'json',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'x-requested-with': 'XMLHttpRequest',
                'Cache-Control': 'max-age=0',
                'Pragma': 'no-cache',
                'Content-Type': 'application/json',
            },
            success: function (res) {
                $('#result').html(syntaxHighlight(res));
            },
            error: function (e) {
                alert_error();
            }
        });
    }

    function logging_query(num) {
        switch (num) {
            case 1:
                var data = JSON.stringify({
                    "method": "get_database_log"
                })
                break;
            case 2:
                var data = JSON.stringify({
                    "method": "get_login_log"
                })
                break;
            case 3:
                var data = JSON.stringify({
                    "method": "get_status_log"
                })
                break;
        }
        let url = 'http://8.137.97.80/north/get'
        $.ajax({
            url: url,
            type: 'post',
            dataType: "json",
            data: data,
            cache: false,
            headers: {
                'dataType': 'json',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'x-requested-with': 'XMLHttpRequest',
                'Cache-Control': 'max-age=0',
                'Pragma': 'no-cache',
                'Content-Type': 'application/json',
            },
            success: function (res) {
                $('#result').html(syntaxHighlight(res[0]));
                    for (var i = 1; i < res.length; ++i){
                        $('#result').append("<br><br>");
                        $('#result').append(syntaxHighlight(res[i]));
                    }
            },
            error: function (e) {
                alert_error();
            }
        });
    }

    function add_group() {
        $.ajax({
            url: 'http://8.137.97.80/north/add',
            type: 'post',
            dataType: "json",
            data: JSON.stringify({
                "version": "1.0",
                "method": "add_group",
                "data": [{ 
                    "group_num": $("#add-group-field #group-num").val(),
                    "group_name": $("#add-group-field #group-name").val(),
                    "description": $("#add-group-field #description").val()
                }]
            }),
            cache: false,
            headers: {
                'dataType': 'json',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'x-requested-with': 'XMLHttpRequest',
                'Cache-Control': 'max-age=0',
                'Pragma': 'no-cache',
                'Content-Type': 'application/json',
            },
            success: function (res) {
                $('#result').html(syntaxHighlight(res));
            },
            error: function (e) {
                alert_error();
            }
        });
    }

    function add_relation() {
        $.ajax({
            url: 'http://8.137.97.80/north/add',
            type: 'post',
            dataType: "json",
            data: JSON.stringify({
                "version": "1.0",
                "method": "add_relation",
                "data":[{
                    "id": $("#add-relation-field #add-relation-group-id").val(),
                    "group_num": $("#add-relation-field #add-relation-group-number").val(),
                }]
            }),
            cache: false,
            headers: {
                'dataType': 'json',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'x-requested-with': 'XMLHttpRequest',
                'Cache-Control': 'max-age=0',
                'Pragma': 'no-cache',
                'Content-Type': 'application/json',
            },
            success: function (res) {
                $('#result').html(syntaxHighlight(res));
            },
            error: function (e) {
                alert_error();
            }
        });
    }

    function get_device_and_group_by_id() {
        $.ajax({
            url: 'http://8.137.97.80/north/get',
            type: 'post',
            dataType: "json",
            data: JSON.stringify({
                "version": "1.0",
                "method": "get_device_and_group_by_id",
                "data":[
                    $("#get-device-and-group-by-id-field #get-device-and-group-by-id-device-id").val()
                ]
            }),
            cache: false,
            headers: {
                'dataType': 'json',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'x-requested-with': 'XMLHttpRequest',
                'Cache-Control': 'max-age=0',
                'Pragma': 'no-cache',
                'Content-Type': 'application/json',
            },
            success: function (res) {
                if (res.result == true) {
                    $('#result').html(syntaxHighlight(res.data[0]));
                } else {
                    $('#result').html(syntaxHighlight(res));
                }
            },
            error: function (e) {
                alert_error();
            }
        });
    }

    function delete_device_by_id() {
        $.ajax({
            url: 'http://8.137.97.80/north/delete',
            type: 'post',
            dataType: "json",
            data: JSON.stringify({
                "version": "1.0",
                "method": "delete_device",
                "data":[
                    $("#delete-device-by-id-field #delete-device-by-id-device-id").val()
                ]
            }),
            cache: false,
            headers: {
                'dataType': 'json',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'x-requested-with': 'XMLHttpRequest',
                'Cache-Control': 'max-age=0',
                'Pragma': 'no-cache',
                'Content-Type': 'application/json',
            },
            success: function (res) {
                $('#result').html(syntaxHighlight(res));
            },
            error: function (e) {
                alert_error();
            }
        });
    }

    function delete_relation_by_id() {
        $.ajax({
            url: 'http://8.137.97.80/north/delete',
            type: 'post',
            dataType: "json",
            data: JSON.stringify({
                "version": "1.0",
                "method": "delete_relation",
                "data":[
                    $("#delete-relation-by-id-field #delete-relation-by-id-device-id").val()
                ]
            }),
            cache: false,
            headers: {
                'dataType': 'json',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'x-requested-with': 'XMLHttpRequest',
                'Cache-Control': 'max-age=0',
                'Pragma': 'no-cache',
                'Content-Type': 'application/json',
            },
            success: function (res) {
                $('#result').html(syntaxHighlight(res));
            },
            error: function (e) {
                alert_error();
            }
        });
    }

    function delete_group_by_number() {
        $.ajax({
            url: 'http://8.137.97.80/north/delete',
            type: 'post',
            dataType: "json",
            data: JSON.stringify({
                "version": "1.0",
                "method": "delete_group",
                "data":[
                    $("#delete-group-by-num-field #delete-group-by-num-group-num2").val()
                ]
            }),
            cache: false,
            headers: {
                'dataType': 'json',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'x-requested-with': 'XMLHttpRequest',
                'Cache-Control': 'max-age=0',
                'Pragma': 'no-cache',
                'Content-Type': 'application/json',
            },
            success: function (res) {
                $('#result').html(syntaxHighlight(res));
            },
            error: function (e) {
                alert_error();
            }
        });
    }

    function get_device_by_group() {
        $.ajax({
            url: 'http://8.137.97.80/north/get',
            type: 'post',
            dataType: "json",
            data: JSON.stringify({
                "version": "1.0",
                "method": "get_device_by_group",
                "data":[
                    $("#get-device-by-group-field #get-device-by-group-group-num2").val()
                ]
            }),
            cache: false,
            headers: {
                'dataType': 'json',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'x-requested-with': 'XMLHttpRequest',
                'Cache-Control': 'max-age=0',
                'Pragma': 'no-cache',
                'Content-Type': 'application/json',
            },
            success: function (res) {
                $('#result').html(syntaxHighlight(res));
            },
            error: function (e) {
                alert_error();
            }
        });
    }

    function syntaxHighlight(json) {
        if (typeof json != 'string') {
            json = JSON.stringify(json, undefined, 2);
        }
        json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function(match) {
            var cls = 'number';
            if (/^"/.test(match)) {
                if (/:$/.test(match)) {
                    cls = 'key';
                } else {
                    cls = 'string';
                }
            } else if (/true|false/.test(match)) {
                cls = 'boolean';
            } else if (/null/.test(match)) {
                cls = 'null';
            }
            return '<span class="' + cls + '">' + match + '</span>';
        });
    }

    function only_show(str) {
        $(".field").hide();
        $("#"+str).show();
        $("#result").empty()
        $("#result").show();
    }

    function alert_error() {
        alert("request error!")
    }
})