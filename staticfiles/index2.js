const week = ["日", "月", "火", "水", "木", "金", "土"];
const today = new Date();
let shukujitu="2021/1/1,元日\n2021/1/11,成人の日\n2021/2/11,建国記念の日\n2021/2/23,天皇誕生日\n2021/3/20,春分の日\n2021/4/29,昭和の日\n2021/5/3,憲法記念日\n2021/5/4,みどりの日\n2021/5/5,こどもの日\n2021/7/22,海の日\n2021/7/23,スポーツの日\n2021/8/8,山の日\n2021/8/9,休日\n2021/9/20,敬老の日\n2021/9/23,秋分の日\n2021/11/3,文化の日\n2021/11/23,勤労感謝の日";
// 月末だとずれる可能性があるため、1日固定で取得
let showDate = new Date(today.getFullYear(), today.getMonth(), 1);
// 初期表示
window.onload = function () {
    showProcess(today);
};
// 前の月表示
function prev(){
    showDate.setMonth(showDate.getMonth() - 1);
    showProcess(showDate);
}
// 次の月表示
function next(){
    showDate.setMonth(showDate.getMonth() + 1);
    showProcess(showDate);
}
// カレンダー表示（来月）
function showProcess(date) {
    let year = date.getFullYear();
    let month;
    if(date.getMonth()!=12){
        month = date.getMonth()+1;
    }else{
        month = 1;
    }
    document.querySelector('#header').innerHTML = year + "年 " + (month + 1) + "月";
    let calendar = createProcess(year, month);
    document.querySelector('#calendar').innerHTML = calendar;
}
// カレンダー作成
function createProcess(year, month) {
    // 曜日
    let calendar = "<table><tr class='dayOfWeek'>";
    for (var i = 0; i < week.length; i++) {
        calendar += "<th>" + week[i] + "</th>";
    }
    calendar += "</tr>";
    let count = 0;
    let startDayOfWeek = new Date(year, month, 1).getDay();
    let endDate = new Date(year, month + 1, 0).getDate();
    let lastMonthEndDate = new Date(year, month, 0).getDate();
    let row = Math.ceil((startDayOfWeek + endDate) / week.length);
    // 1行ずつ設定
    for (let i = 0; i < row; i++) {
        calendar += "<tr>";
        // 1colum単位で設定
        for (let j = 0; j < week.length; j++) {
            if (i == 0 && j < startDayOfWeek) {
                // 1行目で1日まで先月の日付を設定
                calendar += "<td class='disabled'>" + (lastMonthEndDate - startDayOfWeek + j + 1) + "</td>";
            } else if (count >= endDate) {
                // 最終行で最終日以降、翌月の日付を設定
                count++;
                calendar += "<td class='disabled'>" + (count - endDate) + "</td>";
            } else {
                // 当月の日付を曜日に照らし合わせて設定
                count++;
                let dateInfo = checkDate(year, month, count);
                if(dateInfo.isToday){
                    calendar += '<td noWrap class="today">' + count + '<br><input type="radio" name="'+'day'+count+'" value=日替わり checked />ひ<br><input type="radio" name="'+'day'+count+'" value=こだわり />こ<br><input type="radio" name="'+'day'+count+'" value=丼物 />丼<br><input type="radio" name="'+'day'+count+'" value=ラーメン />ラ<br><input type="radio" name="'+'day'+count+'" value=うどん />う<br><input type="radio" name="'+'day'+count+'" value=そば />そ<br><input type="radio" name="'+'day'+count+'" value=欠食 />欠</td>';
                } else if(dateInfo.isHoliday) {
                    calendar += "<td class='holiday' title='" + dateInfo.holidayName + "'>" + count + "</td>";
                } else if(j==0 || j==6){
                    calendar += "<td>" + count + "</td>";
                  }else{
                    calendar += '<td noWrap>' + count + '<input type="radio" name="'+'day'+count+'" value=日替わり checked />ひ<br><input type="radio" name="'+'day'+count+'" value=こだわり />こ<br><input type="radio" name="'+'day'+count+'" value=丼物 />丼<br><input type="radio" name="'+'day'+count+'" value=ラーメン />ラ<br><input type="radio" name="'+'day'+count+'" value=うどん />う<br><input type="radio" name="'+'day'+count+'" value=そば />そ<br><input type="radio" name="'+'day'+count+'" value=欠食 />欠</td>';
                }
            }
        }
        calendar += "</tr>";
    }
    return calendar;
}
// 日付チェック
function checkDate(year, month, day) {
    if(isToday(year, month, day)){
        return {
            isToday: true,
            isHoliday: false,
            holidayName: ""
        };
    }

    var checkHoliday = isHoliday(year, month, day);
    return {
        isToday: false,
        isHoliday: checkHoliday[0],
        holidayName: checkHoliday[1],
    };
}

// 当日かどうか
function isToday(year, month, day) {
    return (year === today.getFullYear()
        && month === (today.getMonth())
        && day === today.getDate());
}
// 祝日かどうか
function isHoliday(year, month, day) {
    let checkDate = year + '/' + (month+1) + '/' + day;
    let dateList = shukujitu.toString().split('\n');
    // 1行目はヘッダーのため、初期値1で開始
    for (var i = 1; i < dateList.length; i++) {
        if (dateList[i].split(',')[0] === checkDate) {
            return [true, dateList[i].split(',')[1]];
        }
    }
    return [false, ""];    
}