for k=1:28801
    name1=mat2str(HasSentiment.('picurl')(k));
    name1=name1(36:45);
    image=imread(strcat('C:\\Users\\Chengbi\\OneDrive - George Mason University\\Research\\WebScraper\\CroppedImages\\',name1,'.png'));
    colorful=colorfulness(image);
%     lab=rgb2lab(image);
%     l = lab(:,:,1);
%     a = lab(:,:,2);
%     b = lab(:,:,3);
%     c = sqrt(a.^2+b.^2);
%     h = atan2d(b,a)+360*(b<0);
%     
%     hs=sum(h,'all');
%     hm=mean(h,'all');
%     hsd=std(h,0,'all');
%     cs=sum(c,'all');
%     cm=mean(c,'all');
%     csd=std(c,0,'all');
%     ls=sum(l,'all');
%     lm=mean(l,'all');
%     lsd=std(l,0,'all');
%     dlmwrite('huesum.txt',hs,'-append')
%     dlmwrite('huemean.txt',hm,'-append')
%     dlmwrite('huestd.txt',hsd,'-append')
%     dlmwrite('chrsum.txt',cs,'-append')
%     dlmwrite('chrmean.txt',cm,'-append')
%     dlmwrite('chrstd.txt',csd,'-append')
%     dlmwrite('lumsum.txt',ls,'-append')
%     dlmwrite('lummean.txt',lm,'-append')
%     dlmwrite('lumstd.txt',lsd,'-append')
    dlmwrite('colorfulness.txt',colorful,'-append')
%     i=3;
%     while (boxes.(i)(k)~= "") 
%         [x,y]=coordinatesconvert(boxes.(i)(k));
%         image=wordremove(image,x,y);
%         i = i+1;
%     end
%     imwrite(image,strcat('C:\\Users\\cliu19\\OneDrive - George Mason University\\Research\\WebScraper\\CroppedImages\\',name1,'.png'));
    k
end

function [x,y] = coordinatesconvert(rawbox)
B = regexp(rawbox,'\d*','Match');
x=[B(1) B(3) B(5) B(7)];
x=str2double(x);
y=[B(2) B(4) B(6) B(8)];
y=str2double(y);
end

function outimg = wordremove(img,x,y)
r = img(:,:,1);
g = img(:,:,2);
b = img(:,:,3);
r = regionfill(r,x,y);
g = regionfill(g,x,y);
b = regionfill(b,x,y);
outimg = cat(3,r,g,b);
end

function colorful=colorfulness(img) 
r = img(:,:,1);
g = img(:,:,2);
b = img(:,:,3);
rg = double(abs(r-g));
yb = double(abs(0.5 * (r + g) - b));

stdRoot = sqrt((std2(rg)).^2 + (std2(yb)).^2);
meanrg=mean(rg,'all');
meanyb=mean(yb,'all');
meanRoot = sqrt(meanrg.^2 + meanyb.^2);

colorful = stdRoot + (0.3 * meanRoot);
end