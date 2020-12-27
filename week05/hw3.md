作业三：请用自己的语言描述如下问题：

- 在你目前的工作场景中，哪个业务适合使用 rabbitmq？

    Ans: 網站的log經由三種parser處理至三個資料庫

- 引入 rabbitmq 主要解决什么问题?（非相关工作可以以设计淘宝购物和结账功能为例来描述）

    Ans: 同時寫入三個資料庫的異步執行，增加效能

- 如何避免消息重复投递或重复消费？

    Ans: 

    MQ-client生成inner-msg-id，保證上半場冪等。

    業務發送方帶入biz-id，業務接收方去重保證冪等。

- 交换机 fanout、direct、topic 有什么区别？

    Ans: 

    1. Fanout Exchange（ 轉發消息最快）：所有發送到Fanout Exchange的消息都會被轉發到與該Exchange 綁定(Binding)的所有Queue上。
    2. Direct Exchange（RouteKey區別）：所有發送到Direct Exchange的消息被轉發到RouteKey中指定的Queue。
    3. Topic Exchange（RouteKey + 某Topic）：所有發送到Topic Exchange的消息被轉發到所有關聯RouteKey中指定Topic的Queue上。

- 架构中引入消息队列是否利大于弊？你认为消息队列有哪些缺点？

    Ans: 

    利: 解耦與復用/異步/異步

    弊: 增加了複雜度與降低了可用性/一致性問題

    並不需要去刻意的尋找消息隊列的使用場景，而是當出現性能瓶頸時，去查看業務邏輯是否存在可以異步處理的耗時操作

作业 3 提示：
（1）服务间异步通信
（2）顺序消费
（3）定时任务
（4）流量削峰
（5）解耦
（6）利用消息队列将高并发访问变为串行操作
（7）异步下单
（8）消息队列持久化
