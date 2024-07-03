import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

def create_visualizations(processed_data):
    visualizations = {}
    
    # Top Artists Bar Chart
    plt.figure(figsize=(10, 6))
    plt.bar(processed_data['top_artists']['artist'], processed_data['top_artists']['popularity'])
    plt.title('Top Artists by Popularity')
    plt.xlabel('Artist')
    plt.ylabel('Popularity')
    plt.xticks(rotation=45, ha='right')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    visualizations['top_artists'] = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close()
    
    # Listening Time Pie Chart
    labels = ['Listening', 'Other']
    sizes = [processed_data['listening_time'], 1440 - processed_data['listening_time']]  # 1440 minutes in a day
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Daily Listening Time')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    visualizations['listening_time'] = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close()
    
    return visualizations