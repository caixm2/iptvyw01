select quju, round(sum(sjjdll),0), sum(sjepgbf), sum(sjbf), round(sum(sjdbkj),0) from thwsheji
where popid not in(2,3,4,19,23,35,37,39,40,49,62)
group by quju
order by substring_index('核心,浦东',quju,2); 

select * from tzteDayRptAreaSum;

create view as 
select  t4.quju quju,  count(t2.tjdbkj/1024) as hejinum, round(sum(t4.sjjdll),0) as hejiwidth , t2.createtime
#        round(sum(t3.smaxoutput),0) as hejioutput, round(sum(t3.smaxoutput)/sum(t4.sjjdll)*100,0) as hejioutputper, 
#        sum(t4.sjepgbf) as hejiepgrl , sum(t2.tjepgsy) as hejiepgsy, round(sum(t2.tjepgsy)/sum(t4.sjepgbf)*100,0) as hejiepgsyl, 
#        sum(t4.sjbf) as hejihmsrl , sum(t2.tjhmssy) as hejihmssy, round(sum(t2.tjhmssy)/sum(t4.sjbf)*100,0) as hejihmssyl, 
 #       round(sum(t2.tjdbkj/1024),2) as heji, round(sum(t2.tjsykj/1024),2) as kjheji, round(sum(t2.tjsykj)/sum(t2.tjdbkj)*100,0) as kjhejisyl
from thwtongji t1 right join thwtongji t2
on t1.popid = t2.upid and t2.popid != 2 and t2.popid != 62
left join vhwethToday t3
on t2.jiedian = t3.sjiedian
left join thwsheji t4
on t2.jiedian = t4.jiedian 
where (unix_timestamp(t2.createtime) > unix_timestamp(date_add(curdate() - day(curdate()) + 1, interval -1 month)) and unix_timestamp(t2.createtime) < date_add(curdate(), interval - day(curdate()) + 1 day))
and (unix_timestamp(t1.createtime) > unix_timestamp(date_add(curdate() - day(curdate()) + 1, interval -1 month)) 
     and unix_timestamp(t1.createtime) < date_add(curdate(), interval - day(curdate()) + 1 day) || 
  t2.popid = '1')
group by t4.quju, date_format(t2.createtime, '%Y-%m-%d')
order by t4.quju, date_format(t2.createtime, '%Y-%m-%d');

