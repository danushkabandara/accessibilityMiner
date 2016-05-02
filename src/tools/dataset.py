import sys
sys.path.append("..")
import matplotlib.pyplot as plt
import model

wa_types_error_dist = {}
wa_types_potential_dist = {}
wa_types_likely_dist = {}

urls = model.WebAccessibility.objects()
for url in urls:
    print url.url
    for key, value in url.type_known.iteritems():
        if int(key) in wa_types_error_dist.keys():
            wa_types_error_dist[int(key)] += value
        else:
            wa_types_error_dist[int(key)] = value

print wa_types_error_dist

x = [i for i in wa_types_error_dist.keys()]
y = [i for i in wa_types_error_dist.values()]
print x

xmax = max(wa_types_error_dist.keys())
ymax = max(wa_types_error_dist.values())
plt.figure()
plt.hist(x, bins=xmax, weights=y, log=True)
plt.title('WA Error Histogram')
plt.xlabel('Error ID')
plt.ylabel('Number of Error')
plt.axis([0, xmax, 0, ymax])
plt.savefig('error_hist.png')


for url in urls:
    print url.url
    for key, value in url.type_potential.iteritems():
        if int(key) in wa_types_potential_dist.keys():
            wa_types_potential_dist[int(key)] += value
        else:
            wa_types_potential_dist[int(key)] = value

print wa_types_potential_dist

x = [i for i in wa_types_potential_dist.keys()]
y = [i for i in wa_types_potential_dist.values()]

xmax = max(wa_types_potential_dist.keys())
ymax = max(wa_types_potential_dist.values())
plt.figure()
plt.hist(x, bins=xmax, weights=y, log=True)
plt.title('WA Potential Histogram')
plt.xlabel('Potential ID')
plt.ylabel('Number of Potential')
plt.axis([0, xmax, 0, ymax])
plt.savefig('potential_hist.png')


for url in urls:
    print url.url
    for key, value in url.type_likely.iteritems():
        if int(key) in wa_types_likely_dist.keys():
            wa_types_likely_dist[int(key)] += value
        else:
            wa_types_likely_dist[int(key)] = value

print wa_types_likely_dist

x = [i for i in wa_types_likely_dist.keys()]
y = [i for i in wa_types_likely_dist.values()]

xmax = max(wa_types_likely_dist.keys())
ymax = max(wa_types_likely_dist.values())
plt.figure()
plt.hist(x, bins=xmax, weights=y, log=True)
plt.title('WA Likely Histogram')
plt.xlabel('Likely ID')
plt.ylabel('Number of Likely')
plt.axis([0, xmax, 0, ymax])
plt.savefig('likely_hist.png')