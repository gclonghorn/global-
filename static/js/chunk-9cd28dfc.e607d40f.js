(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-9cd28dfc"],{"19a5":function(e,t,s){"use strict";var a=s("a939"),n=s.n(a);n.a},"356b":function(e,t,s){},"718c":function(e,t,s){"use strict";var a=s("356b"),n=s.n(a);n.a},a939:function(e,t,s){},e529:function(e,t,s){"use strict";s.r(t);var a=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{directives:[{name:"web-title",rawName:"v-web-title",value:{title:"收件箱"},expression:"{title:'收件箱'}"}],staticClass:"basic"},[s("el-col",{attrs:{span:4}},[s("work-space")],1),s("el-col",{attrs:{span:20}}),s("el-container",[s("el-main",[s("h3",[e._v("收件箱")]),s("div",[s("messageCard",{attrs:{messages:e.messages}}),s("br")],1)]),s("el-aside",{staticStyle:{"text-align":"center",padding:"50px","line-height":"80px"}},[s("div",[s("el-button",{attrs:{type:"warning",plain:""},on:{click:e.readAll}},[e._v("全部已读")])],1),s("div",[!0===e.ifGetAllMessage?s("el-button",{attrs:{type:"primary",plain:""},on:{click:e._getMessage}},[e._v("查看未读")]):e._e()],1),s("div",[!1===e.ifGetAllMessage?s("el-button",{attrs:{type:"primary",plain:""},on:{click:e._getAllMessage}},[e._v("查看全部")]):e._e()],1),s("div",[s("el-button",{attrs:{type:"warning",plain:""},on:{click:e.deleteAll}},[e._v("全部删除")])],1)])],1)],1)},n=[],i=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",e._l(e.messages,(function(t){return s("div",{key:t.label},[s("el-card",{staticStyle:{width:"500px"}},[s("el-container",[s("el-col",{attrs:{span:"3"}},[1===t.type?s("i",{staticClass:"el-icon-user",staticStyle:{"margin-top":"40%","margin-left":"10px"}}):e._e(),2===t.type?s("i",{staticClass:"el-icon-s-comment",staticStyle:{"margin-top":"40%","margin-left":"10px"}}):e._e(),3===t.type?s("i",{staticClass:"el-icon-close",staticStyle:{"margin-top":"40%","margin-left":"10px"}}):e._e(),4===t.type?s("i",{staticClass:"el-icon-error",staticStyle:{"margin-top":"40%","margin-left":"10px"}}):e._e(),5===t.type?s("i",{staticClass:"el-icon-user",staticStyle:{"margin-top":"40%","margin-left":"10px"}}):e._e(),6===t.type?s("i",{staticClass:"el-icon-chat-line-round",staticStyle:{"margin-top":"40%","margin-left":"10px"}}):e._e(),7===t.type?s("i",{staticClass:"el-icon-chat-round",staticStyle:{"margin-top":"40%","margin-left":"10px"}}):e._e(),8===t.type?s("i",{staticClass:"el-icon-close",staticStyle:{"margin-top":"40%","margin-left":"10px"}}):e._e(),9===t.type?s("i",{staticClass:"el-icon-error",staticStyle:{"margin-top":"40%","margin-left":"10px"}}):e._e()]),s("el-col",{staticStyle:{"margin-top":"10px"}},[s("el-row",[s("div",{staticClass:"title"},[e._v(e._s(t.origin_user.username)+e._s(t.content))])]),s("el-row",[s("div",{staticClass:"details"},[e._v(e._s(t.document.name))])]),s("br"),s("el-row",[s("el-col",{attrs:{span:"14"}},[s("time",{staticClass:"time"},[e._v(e._s(t.time))])]),s("el-button",{attrs:{type:"text",icon:"el-icon-close"},on:{click:function(s){return e.deleteMessage(t.id)}}},[e._v("删除")]),s("el-divider",{attrs:{direction:"vertical"}}),0===t.status?s("el-button",{attrs:{type:"text",icon:"el-icon-check"},on:{click:function(s){return e.readMessage(t.id,t.status)}}},[e._v("标为已读")]):e._e(),1===t.status?s("el-button",{attrs:{type:"text",disabled:"true"}},[e._v("已读")]):e._e()],1)],1)],1)],1),s("br")],1)})),0)},l=[],c=s("4ec3"),o={name:"messageCard",props:{messages:{type:Array,required:!0}},methods:{readMessage:function(e,t){1===t?t=0:0===t&&(t=1),Object(c["B"])(e,t).then((function(e){e.status,console.log(e)}))},deleteMessage:function(e){Object(c["h"])(e).then((function(e){e.status,console.log(e)}))}}},r=o,g=(s("19a5"),s("2877")),m=Object(g["a"])(r,i,l,!1,null,null,null),u=m.exports,p=s("56d7"),d={data:function(){return{ifGetAllMessage:!0,messages:[{id:15,user:{id:1,username:"1",head:null},origin_user:{id:2,username:"1679",head:null},document:{id:1,name:"测试"},time:"2020-08-15T22:03:10.828014",type:6,status:1},{id:15,user:{id:1,username:"1",head:null},origin_user:{id:2,username:"1679",head:null},document:{id:1,name:"测试"},time:"2020-08-15T22:03:10.828014",type:6,status:1},{id:15,user:{id:1,username:"1",head:null},origin_user:{id:2,username:"1679",head:null},document:{id:1,name:"测试"},time:"2020-08-15T22:03:10.828014",type:6,status:1},{id:15,user:{id:1,username:"1",head:null},origin_user:{id:2,username:"1679",head:null},document:{id:1,name:"测试"},time:"2020-08-15T22:03:10.828014",type:6,status:1}]}},components:{messageCard:u},methods:{_getAllMessage:function(){var e=this;Object(c["t"])().then((function(t){if(200===t.status){e.ifGetAllMessage=!0,console.log(t),e.messages=t.data;for(var s=0;s<e.messages.length;s++)e.messages[s].time=Object(p["GetTime"])(e.messages[s].time,"."),1===e.messages[s].type?e.messages[s].content="邀请你加入团队":2===e.messages[s].type?e.messages[s].content="回复了你的团队邀请":3===e.messages[s].type?e.messages[s].content="退出了团队":4===e.messages[s].type?e.messages[s].content="将你移出团队":5===e.messages[s].type?e.messages[s].content="邀请你成为协作者":6===e.messages[s].type?e.messages[s].content="评论了你的文档":7===e.messages[s].type?e.messages[s].content="回复了你的评论":8===e.messages[s].type?e.messages[s].content="退出了文档协作者":9===e.messages[s].type&&(e.messages[s].content="将你移出文档协作者")}}))},_getMessage:function(){var e=this;Object(c["u"])().then((function(t){if(200===t.status){e.ifGetAllMessage=!1,console.log(t),e.messages=t.data;for(var s=0;s<e.messages.length;s++)e.messages[s].time=Object(p["GetTime"])(e.messages[s].time,"."),1===e.messages[s].type?e.messages[s].content="邀请你加入团队":2===e.messages[s].type?e.messages[s].content="回复了你的团队邀请":3===e.messages[s].type?e.messages[s].content="退出了团队":4===e.messages[s].type?e.messages[s].content="将你移出团队":5===e.messages[s].type?e.messages[s].content="邀请你成为协作者":6===e.messages[s].type?e.messages[s].content="评论了你的文档":7===e.messages[s].type?e.messages[s].content="回复了你的评论":8===e.messages[s].type?e.messages[s].content="退出了文档协作者":9===e.messages[s].type&&(e.messages[s].content="将你移出文档协作者")}}))},readAll:function(){var e=this;Object(c["A"])(localStorage.userId).then((function(t){200===t.status?(console.log(t),e._getAllMessage()):console.log(t)}))},deleteAll:function(){var e=this;Object(c["d"])(localStorage.userId).then((function(t){200===t.status?(console.log(t),e._getAllMessage):console.log(t)}))}},mounted:function(){this._getAllMessage()},watch:{messages:{handler:function(e,t){console.log(e),console.log(t),e!==t&&(!0===this.ifGetAllMessage?this._getAllMessage():!1===this.ifGetAllMessage&&this._getMessage())},deep:!0}}},y=d,f=(s("718c"),Object(g["a"])(y,a,n,!1,null,null,null));t["default"]=f.exports}}]);