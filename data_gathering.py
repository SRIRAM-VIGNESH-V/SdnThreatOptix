import influxdb, sys
QUERY = """SELECT DERIVATIVE(icmp_inechos) AS d_ping FROM net ORDER BY time DESC LIMIT 100"""
n_samples, mean = 0, 0
if __name__ == "__main__":  
    db = influxdb.InfluxDBClient('10.0.123.3', 8086, 'influx', 'Password123', 'h4_net_stats')
    measurement_class = sys.argv[1]
    out_file = open("ICMP_data_class_{}.csv".format(measurement_class), "w+")
    for measurement in db.query(QUERY).get_points(measurement = 'net'):
        curr_derivative = measurement["d_ping"]
        n_samples += 1
        delta_mean = (curr_derivative - mean) / n_samples
        mean += delta_mean
        out_file.write("{}, {}, {}\n".format(curr_derivative, mean, measurement_class))
    out_file.close()
    print("Finished generating a class {} training dataset!".format(measurement_class))
    exit(0)