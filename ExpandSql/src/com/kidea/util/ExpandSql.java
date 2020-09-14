package com.kidea.util;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.apache.commons.lang3.StringUtils;

/**
 * Lets code and celebrate the 'Engineering Productivity' cerner_2^5_2020
 * Expand the sql string with n number of '?' symbol based on query parameter list passed in.
 * @author Kingsly, Philomin Irudayaraj
 *
 */
public class ExpandSql {
	public static void main(String[] args) {
		String sql = "select * from tableABC where columnA in ( %s )";
		List<String> columnAValues = new ArrayList<>();
		columnAValues.add("ABC");
		columnAValues.add("DEF");
		columnAValues.add("GHI");
		columnAValues.add("JKL");
		//Expand '?' number of times based on the input list
		String expandSqlStr = StringUtils.join(Collections.nCopies(columnAValues.size(), "?"), ", ");
		//Format the string by replacing with expanded '?' string.
		System.out.println(String.format(sql, expandSqlStr));
	}
}
