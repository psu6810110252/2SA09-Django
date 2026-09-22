class Sushi {
  final String title;
  final String description;
  final double price;
  final String imageUrl;

  Sushi({
    required this.title,
    required this.description,
    required this.price,
    required this.imageUrl,
  });
}

List<Sushi> sushiMenu = [
  Sushi(
    title: 'ซูชิไข่หวาน',
    description: 'ข้าวปั้นหน้าดาชิมากิหรือไข่หวานญี่ปุ่นแท้ รสกลมกล่อมหอมหวาน เนื้อนุ่มละมุนละไม เข้ากันดีกับข้าวซูชิปรุงรส',
    price: 10,
    imageUrl: 'assets/images/sushi_1.png',
  ),
  Sushi(
    title: 'ซูชิหน้าปลาแซลมอน',
    description: 'ซูชิหน้าปลาแซลมอนสดคุณภาพพรีเมียม สไลซ์บางพอดีคำ เนื้อนุ่มลิ้น มันแทรกกำลังดี หอมกลิ่นทะเลธรรมชาติ',
    price: 20,
    imageUrl: 'assets/images/sushi_2.png',
  ),
  Sushi(
    title: 'ซูชิหน้าไข่กุ้ง',
    description: 'ข้าวซูชิราดด้วยไข่กุ้งสีส้มสด เคี้ยวเพลิน กรุบกรอบเบาๆ ทุกคำ พร้อมสัมผัสรสชาติจากทะเลแบบเต็มๆ',
    price: 15,
    imageUrl: 'assets/images/sushi_3.png',
  ),
  Sushi(
    title: 'ซูชิหน้ากุ้งผีเสื้อ',
    description: 'กุ้งสดลวกพอดีตัว ผ่ากลางจัดเรียงแบบผีเสื้อ วางบนข้าวซูชิร้อนๆ เพิ่มความหวานธรรมชาติจากเนื้อกุ้งแน่นๆ',
    price: 15,
    imageUrl: 'assets/images/sushi_4.png',
  ),
  Sushi(
    title: 'ซูชิหน้าปูอัด',
    description: 'ข้าวซูชิหอมๆ จับคู่กับปูอัดเนื้อนุ่มแน่น รสชาติเข้มข้น ท็อปด้วยมายองเนสเบาๆ เพิ่มความกลมกล่อมในคำเดียว',
    price: 10,
    imageUrl: 'assets/images/sushi_5.png',
  ),
  Sushi(
    title: 'ซูชิหน้าหอยลายปรุงรส',
    description: 'หอยลายปรุงรสญี่ปุ่น เคี้ยวสนุก รสหวานเค็มกลมกล่อม วางบนข้าวซูชิร้อนๆ เติมเต็มความอร่อยสไตล์ดั้งเดิม',
    price: 15,
    imageUrl: 'assets/images/sushi_6.png',
  ),
  Sushi(
    title: 'ซูชิหน้ายำสาหร่าย',
    description: 'ยำสาหร่ายญี่ปุ่นรสเปรี้ยวหวาน เค็มนิด เผ็ดหน่อย เสิร์ฟบนข้าวซูชิ อุดมด้วยไฟเบอร์ และรสชาติสดชื่นจากท้องทะเล',
    price: 10,
    imageUrl: 'assets/images/sushi_7.png',
  ),
  Sushi(
    title: 'ซูชิหน้าทูน่าสลัด',
    description: 'ข้าวซูชิร้อนๆ ท็อปด้วยทูน่าสลัดเนื้อแน่น คลุกเคล้าด้วยมายองเนสรสละมุน กินง่าย อร่อยได้ทุกวัย',
    price: 10,
    imageUrl: 'assets/images/sushi_8.png',
  ),
  
];